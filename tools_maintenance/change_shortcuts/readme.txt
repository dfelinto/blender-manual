change_shortcuts
================

Scripts to bulk change shortcut (:kbd:`...`) and menu item (:menuselection:`...`) names.
Use with care!!



change_man_shortcuts.py
-----------------------
It changes all the shortcuts and menu items in RST files of the the manual according
to a CSV substitution table. If one of the entries in the table is, for instance:

LMB;LeftMouse

then all related shortcuts will be replaced, that is:

    :kbd:`LMB`       becomes  :kbd:`LeftMouse`
    :kbd:`Ctrl-LMB`  becomes  :kbd:`Ctrl-LeftMouse`
    Etc.

The file 'table.csv' must be in the same folder as the script.

On completion, a 'new_manual' subfolder will be created in the script folder.
In it, you will find all the RST files that were changed. You can check them
before dumping and replacing the desired files onto the repository.



change_tr_shortcuts.py
----------------------
Same thing as 'change_man_shortcuts.py', but for translations.
You must specify a language (e.g. 'es'), and provide a substitution table
(e.g. 'table_es.csv') in the same folder as the script.

Substitutions will be performed only in 'msgstr' strings in the PO files.

It will generate a 'new_locale' subfolder in wich all replaced PO files for
the desired language will be found.



diff_man_shortcuts.py
---------------------
Useful for checking all the differences between the newly generated RST files
and the current files in the repository. A file 'diff_man.txt' will be generated
in the script folder, with all the differences.



diff_tr_shortcuts.py
---------------------
Same as 'diff_man_shortcuts.py', but for translation files. Language must be indicated
(e.g. 'fr'), and the corresponding diff text file will be created (e.g. 'diff_fr.txt')
in the script folder.



clear_temp_data.py
------------------
It deletes all temporary data, if they exist: 'new_manual' and 'new_locale' subfolders,
as well as all diff files.



list_man_shortcuts.py
--------------------
Shows two lists: one for all the :kbd: items, and one for all the :menuselection: items
present in the RST files of the manual. Lists are alphabetically sorted.
This is useful to check that all the items have a right format. To locate which files
contain a specific name, use 'find_man_shortcuts.py'.



list_tr_shortcuts.py
--------------------
Same as 'list_man_shortcuts.py', but for a specific language translation (items in 'msgstr' strings
in PO files). To locate which files contain a specific name, use 'find_tr_shortcuts.py'.



find_man_shortcuts.py
---------------------
Used to find which RST files in the repository contain a specific exact name in a :kbd: or :menuselection: item.



find_tr_shortcuts.py
--------------------
The same as 'find_man_shortcuts.py' but searching only in 'msgstr' strings in the PO files of
the specified translation.

