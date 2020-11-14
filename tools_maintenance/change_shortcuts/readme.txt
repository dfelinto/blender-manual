change_shortcuts
================

Scripts to bulk change shortcut names (:kbd:`...`).



change_man_shortcuts.py
-----------------------

It changes all the shortcuts in the manual according to a CSV substitution table.
If one of the entries is, for instance:

LMB;LeftMouse

then all related shortcuts will be replaced, that is:

    :kbd:`LMB`       becomes  :kbd:`LeftMouse`
    :kbd:`Ctrl-LMB`  becomes  :kbd:`Ctrl-LeftMouse`
    Etc.

The file 'table.csv' must be in the same folder as the script.

On completion, a 'new_manual' subfolder will be created in the script folder.
In it, you will find all the RST files that had replacements. You can check them
before dumping and replacing the desired files onto the repository.



change_tr_shortcuts.py
----------------------

It does the same thing as 'change_man_shortcuts.py', but for translations.
You must specify a language (e.g. 'es'), and provide a substitution table
(e.g. 'table_es.csv') in the same folder as the script.

Substitutions will be performed only in 'msgstr' strings in the PO files.

It will generate a 'new_locale' subfolder in wich all replaced PO files for
the desired language will be found.



diff_man_shortcuts.py
---------------------

Useful for checking all the differences between the newly generated RST files
and the current files in the repository. a file 'diff_man.txt' will be generated
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

