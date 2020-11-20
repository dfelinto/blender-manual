#! /usr/bin/env python3

# Changes the shortcuts (:kbd:`...`) across all the translated PO files
# of a spcecific language, according to the provided JSON table.
# Language code and output directory must be provided.

import json
import sys
import os
import re

ROLE = ':kbd:'  # Change to any other role if needed


def find_vcs_root(dirs=(".svn", ".git"), default=None):
    """
    Returns the repo root dir.

    :param dirs: dirs to look for, for repo detection.
    :param default: value to return if not found.
    :return: repo root dir.
    """
    prev, test = None, os.path.abspath(os.path.dirname(__file__))
    while prev != test:
        if any(os.path.isdir(os.path.join(test, d)) for d in dirs):
            return test
        prev, test = test, os.path.abspath(os.path.join(test, os.pardir))
    return default


def msgstr_replace(msgstr):
    """
    Replaces and returns the provided string based on the substitution table.

    Function attribute 'table' contains the substitution table, as a list of
    2-tuples with replacements for the language of the form
    (regex object, replacement string).
    :param msgstr: string to process.
    :return: replaced string, number of changes made.
    """
    ntotal = 0
    for regex, repl in msgstr_replace.table:
        msgstr, n = regex.subn(repl, msgstr)
        ntotal += n
    return msgstr, ntotal


def file_process(filename):
    """
    Processes the given file. If changes are made, output file is generated.

    :param filename: the path and name of the file to process.
    :return: nothing.
    """
    out_text = ''
    n_changes = 0
    with open(filename, 'rt') as f:
        msgstr = ''
        for line in f:
            if msgstr:
                if line.startswith('"'):
                    msgstr += line
                else:
                    newtext, n = msgstr_replace(msgstr)
                    out_text += newtext + line
                    n_changes += n
                    msgstr = ''
            else:
                if line.startswith('msgstr'):
                    msgstr += line
                else:
                    out_text += line
    if msgstr:  # is there a last pending msgstr?
        newtext, n = msgstr_replace(msgstr)
        out_text += newtext
        n_changes += n
    # In case there were changes, an output file is generated:
    if n_changes > 0:
        print(filename[filename.find('LC_MESSAGES')+11:] + ':',
              n_changes, 'change(s).')
        file_out = os.path.join(os.path.expanduser(sys.argv[2]),
                                'new_' + filename[filename.find('locale'):])
        os.makedirs(os.path.dirname(file_out), exist_ok=True)
        with open(file_out, 'wt') as f:
            f.write(out_text)


def json_parse(obj):
    """
    Function used to parse the json file.

    :param obj: tuple passed by 'json.load()'.
    :return: if 'obj' is top level, it returns the table in a list of 2-tuples,
             or None if table not found, or duplicate elements present.
             If not on top level, it just returns the passed object.
    """
    retval = obj
    if isinstance(obj[0][1], list):  # top level?
        retval = None  # language table not found so far
        for tpl in obj:
            if tpl[0] == sys.argv[1]:  # table found?
                retval = tpl[1]
                break
        if retval:  # table was found?
            # Let's check for duplicates:
            test_set = set(retval)
            if len(test_set) < len(retval):  # duplicates?
                print(f"Error: '{sys.argv[1]}' table contains duplicate entries.")
                retval = None
        else:
            print(f"Error: '{sys.argv[1]}' table not found.")
    return retval


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
elif len(sys.argv) != 3:
    print("""\nUsage: po_shortcuts.py <LANGUAGE> <FOLDER>\n
    Examples: po_shortcuts.py es ~/test
              po_shortcuts.py fr d:\\test\n
    Substitution table needed in 'po_shortcuts_tables.json'.
    Script and tables file must be in the same folder.\n
    Output files will be created in 'new_locale' subfolder
    inside the provided folder in your computer.""")
elif not os.path.isdir(os.path.join(root_path, 'locale', sys.argv[1])):
    print("'<repo_root>/locale/" + sys.argv[1] + "' folder not found. "
          "Script must be in a folder inside the repository.")
elif not os.path.isfile('po_shortcuts_tables.json'):
    print("'po_shortcuts_tables.json' file not found. "
          "Script and tables file must be in the same folder.")
elif not os.path.isdir(os.path.expanduser(sys.argv[2])):
    print("'" + sys.argv[2] + "' folder not found.")
else:  # All OK
    # Reading substitution table. It will be stored as a list of tuples
    # (regex object, replace string) in function attribute 'table' of
    # msgstr_replace() function:
    with open('po_shortcuts_tables.json', 'rt') as ftab:
        table = json.load(ftab, object_pairs_hook=json_parse)
    if table:  # table found and no duplicates?
        msgstr_replace.table = []
        for src, dst in table:
            pattern = r'(' + ROLE + r')("\n")?(`[^`]*?)\b' + src + r'\b([^`]*?`)'
            replace = r'\1\2\3' + dst + r'\4'
            msgstr_replace.table.append((re.compile(pattern, re.MULTILINE),
                                         replace))
        # Main loop:
        for wpath, wdirs, wfiles in os.walk(os.path.join(root_path, 'locale',
                                                         sys.argv[1],
                                                         'LC_MESSAGES')):
            for fname in wfiles:
                path_full = os.path.join(wpath, fname)
                if path_full[-3:] == '.po':
                    file_process(path_full)
