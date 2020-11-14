#! /usr/bin/env python3

# Searches for files containing :kbd: or :menuselection: items that
# match the provided string in the 'msgstr' strings of the desired
# language PO files in the repository.
# Language must be indicated.

import os
import sys

file_list = set()


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


def line_search(line, prefix):
    """
    It searches for the item in the string.
    :param line: the line from the PO file.
    :param prefix: type of element (:kbd:, :menuselection:,...).
    :return: True if found, otherwise False.
    """
    if line.find(prefix + '`' + sys.argv[2] + '`') != -1:
        return True
    return False


def file_process(filename):
    """
    It processes the PO file searching for items.
    :param filename: the name of the PO file.
    :return: nothing.
    """
    global file_list
    fin = open(filename, 'rt')
    in_msgstr = False
    for line in fin:
        if in_msgstr:
            if line[0] == '"':  # still inside a msgstr
                if line_search(line, ':kbd:') or line_search(line, ':menuselection:'):
                    file_list.add(filename)
            else:
                in_msgstr = False  # not anymore in a msgstr
        else:
            if line[:6] == 'msgstr':  # entering a msgstr
                in_msgstr = True
                if line_search(line, ':kbd:') or line_search(line, ':menuselection:'):
                    file_list.add(filename)
    fin.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
elif len(sys.argv) != 3:
    print("""\nUsage: list_tr_shortcuts.py <LANGUAGE> <STRING>

    Examples: list_tr_shortcuts.py es Ctrl
              list_tr_shortcuts.py fr 'View --> Frame All'\n""")
elif not os.path.isdir(os.path.join(root_path, 'locale', sys.argv[1])):
    print("'<repo_root>/locale/" + sys.argv[1] + "' folder not found.")
else:  # All OK
    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'locale', sys.argv[1], 'LC_MESSAGES')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-3:] == '.po':
                file_process(path_full)

    print('Searching for ' + sys.argv[2] + '...')
    for f in file_list:
        print(f[f.find('LC_MESSAGES')+11:])
