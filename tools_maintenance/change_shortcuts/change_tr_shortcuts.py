#! /usr/bin/env python3

# Changes the shortcuts (:kbd:`...`) and menu items (:menuselection:`...`)
# across all the translated PO files of a spcecific language, according to
# the provided CSV table.
#
# Language must be indicated.

import os
import sys


def find_vcs_root(dirs=(".svn", ".git"), default=None):
    """
    Returns the repo root dir.
    :param dirs: dirs to look for.
    :param default: value to return if not found.
    :return: repo root dir.
    """
    prev, test = None, os.path.abspath(os.path.dirname(__file__))
    while prev != test:
        if any(os.path.isdir(os.path.join(test, d)) for d in dirs):
            return test
        prev, test = test, os.path.abspath(os.path.join(test, os.pardir))
    return default


def st_replace(s):
    """
    Replaces the shortcut string, based on the substitution table.
    :param s: shortcut string inside :kbd:`...`.
    :return: replaced string.
    """
    result = s
    for entry in st_replace.table:
        result = result.replace(entry[0], entry[1])
    return result


def line_process(line, line_prev, prefix):
    """
    It processes a line from the PO file.
    :param line: the line from the PO file.
    :param line_prev: previous line in a multi-line 'msgstr'.
    :param prefix: prefix to search (like ':kbd:' or ':menuselection:').
    :return: the processed (replaced) line and the number of changes made.
    """
    result = ''
    n_changes = 0

    # Prefix at the end of the previous line?:
    if line_prev[-(len(prefix) + 2): -2] == prefix:  # ...:prefix:"\n
        assert line[0:2] == '"`'
        result += '"`'
        line = line[2:]
        pos = line.find('`')  # we assume it will be found
        s_in = line[:pos]  # candidate shortcut string to suffer replacements
        s_out = st_replace(s_in)
        result += s_out
        line = line[pos:]
        if s_in != s_out:
            n_changes += 1

    # Rest of prefixes (if any) are fully included in the line:
    while True:
        # Prefix search:
        pos = line.find(prefix + '`')
        if pos != -1:
            result += line[:pos + len(prefix) + 1]
            line = line[pos + len(prefix) + 1:]
        else:
            result += line
            break
        # Shortcut end search
        pos = line.find('`')  # we assume it will be found
        s_in = line[:pos]  # candidate shortcut string to suffer replacements
        s_out = st_replace(s_in)
        result += s_out
        line = line[pos:]
        if s_in != s_out:
            n_changes += 1
    return result, n_changes


def file_process(filename, prefix):
    """
    It processes the PO file to replace and generates the output file
    if changes where necessary.
    :param filename: the name of the PO file.
    :param prefix: prefix to search (like ':kbd:' or ':menuselection:').
    :return: nothing.
    """
    fin = open(filename, 'rt')
    fout_list = []  # text lines of the output file
    in_msgstr = False
    n_changes = 0
    line_prev = ''  # last processed line
    for line in fin:
        if in_msgstr:
            if line[0] == '"':  # still inside a msgstr
                line_out, n = line_process(line, line_prev, prefix)
                line_prev = line
                n_changes += n
            else:
                in_msgstr = False  # not anymore in a msgstr
                line_out = line
                line_prev = ''
        else:
            if line[:6] == 'msgstr':  # entering a msgstr
                in_msgstr = True
                line_out, n = line_process(line, line_prev, prefix)
                line_prev = line
                n_changes += n
            else:  # still outside a msgstr
                line_out = line
        fout_list.append(line_out)
    fin.close()

    # In case there were changes, we generate an output file
    if n_changes > 0:
        print(filename[filename.find('LC_MESSAGES')+11:] + ':',
              n_changes, "change(s).")
        file_out = 'new_' + filename[filename.find('locale'):]
        os.makedirs(os.path.dirname(file_out), exist_ok=True)
        fout = open(file_out, 'wt')
        fout.writelines(fout_list)
        fout.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
elif len(sys.argv) != 2:
    print("""\nUsage: change_tr_shortcuts.py <LANGUAGE>

    Examples: change_tr_shortcuts.py es
              change_tr_shortcuts.py fr

    Substitution table needed (table_<LANGUAGE>.csv).
    Script and table must be in the same folder.

    Output files will be created in 'new_locale' subfolder
    inside the script's folder.\n""")
elif not os.path.isdir(os.path.join(root_path, 'locale', sys.argv[1])):
    print("'<repo_root>/locale/" + sys.argv[1] + "' folder not found.")
elif not os.path.isfile(os.path.join('table_' + sys.argv[1] + '.csv')):
    print("'table_" + sys.argv[1] + ".csv' file not found. "
          "Script and table must be in the same folder.")
else:  # All OK
    # Substitution table initialization. It will be stored as a "static"
    # variable of st_replace() function:
    st_replace.table = []
    f = open('table_' + sys.argv[1] + '.csv', 'rt')
    for ln in f:
        row = ln.strip()
        if row != '' and row[0] != '#':
            r = row.split(';')
            st_replace.table.append((r[0].strip(), r[1].strip()))
    f.close()

    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'locale', sys.argv[1], 'LC_MESSAGES')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-3:] == '.po':
                file_process(path_full, ':kbd:')
                file_process(path_full, 'menuselection')
