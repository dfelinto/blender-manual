#!/bin/bash
# Apache License, Version 2.0

# This script is to reduce tedious steps involved when updating PO files.
# It helps replacing generated placeholders string in your PO files, especially
# when updating PO files, automatically inserting name of author and revision time,
# which should save you some times.
# Recommend to copy this to your $HOME/bin directory and add executable flag (chmod u+x),
# then use it with the directory of your local repository (svn or git), ie.
# 		$HOME/bin/change_placeholders.sh $BLENDER_MAN_EN
# Windows users can try to install Linux on Windows following this guide (https://docs.microsoft.com/en-us/windows/wsl/install-win10)
# Author: Hoang Duy Tran <hoangduytran1960@googlemail.com>
# Revision Date: 2018-11-16 21:19+0000
#
YOUR_NAME="Your Name"
YOUR_EMAIL="your-email@some-server.com"
YOUR_ID="$YOUR_NAME <$YOUR_EMAIL>"
YOUR_TRANSLATION_TEAM="your town/city, Country <$YOUR_EMAIL>"
YOUR_LANGUAGE_CODE="vi"

#executable date, change it to the actual location of your date binary
date_bin=$(which date)
#get the timenow with format '2018-11-16 20:54+0000' - depending on the timezone you are in
time_now=$($date_bin +"%F %H:%M%z")
#the replace string for revision date, which include the time_now value
po_revision_date_value="PO-Revision-Date: ${time_now}"

#the list of pattern to find and the value strings to be replaced
declare -A pattern_list=(
["FIRST AUTHOR.*SS>"]="$YOUR_ID"
["Last-Translator.*>"]="Last-Translator: $YOUR_ID"
["PO-Revision-Date.*[[:digit:]]\{4\}"]="$po_revision_date_value"
["PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE"]="$po_revision_date_value"
["Language-Team:.*>"]="Language-Team: $YOUR_TRANSLATION_TEAM"
)

#This is for the language line. This line is required by POEdit, if you're using it for editing PO files.
#Inserting this line before the MIME-Version.
re_language_code="Language:.*$YOUR_LANGUAGE_CODE"
language_code="\"Language: $YOUR_LANGUAGE_CODE\\\\n\"\n"
declare -A pattern_insert=(
["\"MIME-Version"]="$language_code\"MIME-Version"
)

RE_COMMENTED_LINE="^#~.*$"

#Find the changed files in the local repository, using 'git status' and 'svn status'.
function findChangedFiles()
{
   if [ -d ".git" ]; then
      changed_list=$(git status | grep 'modified' | awk '{ print $2 }' | grep ".po")
   elif [ -d ".svn" ]; then
      changed_list=$(svn status | grep '^M' | awk '{ print $2 }' | grep ".po")
   else #slowest option of all, find po files in any root directory
      changed_list=$(find . -type f -name "*.po" -exec ls -al --time-style=+%D\ %H:%M:%S {} \; | grep `$date_bin +%D` | awk '{ print $6,$7,$8 }' | sort | tail -1 | awk '{ print $3 }')
   fi
}

#Remove all commented line after update_po is executed
#find in all directories just in case old files are still there.
function removeCommentedLineInAllFiles()
{
    po_file_list=$(find . -type f -name "*.po")
    for f in ${po_file_list}; do
		removeCommentedLineInSingleFile $f
    done
}

#Remove commented line in a single file
function removeCommentedLineInSingleFile()
{
	orig_file=$1
	tempfile="temp_file.po"
	exclude_lines=$(grep "$RE_COMMENTED_LINE" $orig_file)
    if [ ! -z "$exclude_lines" ]; then
		grep -v "$RE_COMMENTED_LINE" $orig_file > $tempfile
        mv $tempfile $orig_file
	fi
}


#Replace and report changes based on the differences of sha256sums before and after
function replaceAndReport()
{
	changed_file="$1"
	pattern="$2"
	value="$3"
	shasum_before=$(sha256sum $changed_file |  awk '{ print $1 }')
	sed -i "s|${pattern}|${value}|g" $changed_file
	shasum_after=$(sha256sum $changed_file |  awk '{ print $1 }')
	if [ "$shasum_before" != "$shasum_after" ]; then
		echo "Replaced: $pattern => $value"
	fi
}

#Replacing placeholders as specified in pattern_list array
function replaceRegularStrings()
{
	changed_file="$1"
	for i in "${!pattern_list[@]}"; do
		pattern="$i"
		value="${pattern_list[$i]}"
		replaceAndReport "$changed_file" "$pattern" "$value"
   done
}

#Test for duplication and inserting 'language=<value>' if it hasn't been inserted before
function insertLanguageCode()
{
   changed_file="$1"
   current_line=$(grep $re_language_code $changed_file)
   #echo "current_line=[$current_line]"
   if [ "$current_line" != "" ]; then
      echo "has Language code"
   else
      for i in "${!pattern_insert[@]}"; do
            pattern="$i"
            value="${pattern_insert[$i]}"
            replaceAndReport "$changed_file" "$pattern" "$value"
      done
   fi
}

#Listing out the changed file's content for debugging. By default the listing of content
#is disabled, uncomment the 'cat' line for listing out changes.
#Note, the 'cat' command on Linux/iOS is equivalent of 'type' on Windows
#Make use of the output of 'Updated file...' to help in your comment for svn commit -m ""
#ie. svn commit --username <my_user_name> -m "Inserted translations for ~/...", where '...' is the
#copy of the name of modified file displayed.
function listFileContent()
{
   changed_file=$1
   #cat $changed_file
   echo "Updated file: [$changed_file]"
}

#Perform changing of all files.
#After the initial run through all files on your local HDD, you can comment out lines which you
#no longer needed, such as insertLanguageCode, inserting '#' infront of the line.
function replaceAllChangedFiles()
{
   #removeCommentedLineInAllFiles
   findChangedFiles
   for f in $changed_list; do
	  removeCommentedLineInSingleFile $f
      replaceRegularStrings $f
      insertLanguageCode $f
      listFileContent $f
   done
}

#MAIN portion of your script
#take current_working_directory (cwd) as the 1st element of script parameter
#then change the directory to the one provided.
#Notice the use of environment variables. If you're using some directory constantly then comment
#out this section and directory using 'cd $SOME_DIRECTORY' directly.
cwd=$1
if [[ ! -z  "$cwd" ]]; then
   echo "Using $cwd"
   cd $cwd
else
   echo "Using $BLENDER_MAN_EN/locale"
   cd "$BLENDER_MAN_EN/locale"
fi

#Running the replace for all changed files
replaceAllChangedFiles
