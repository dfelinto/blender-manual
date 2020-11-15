#! /usr/bin/env python3

# Shows a list of all the :kbd: and :menuselection: items present in the
# 'msgstr' strings of the desired language PO files in the repository.
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


def line_search(line, prefix, sc_set):
    """
    It searches for items in a line from the PO file.
    :param line: the line from the PO file.
    :param prefix: type of item (:kbd:, :menuselection:,...).
    :param sc_set: the set where to add the items found.
    :return: nothing.
    """
    while True:
        # shortcut start search
        pos = line.find(prefix + '`')
        if pos == -1:
            break
        line = line[pos+len(prefix)+1:]

        # shortcut end search
        pos = line.find('`')  # we assume it will be found
        s_in = line[:pos]  # string to add to the set
        sc_set.add(s_in)
        line = line[pos:]


def file_process(filename, prefix, sc_set):
    """
    It processes the PO file searching for items.
    :param filename: the name of the PO file.
    :param prefix: prefix to look for (':kbd:' or ':menuselect:').
    :param sc_set: set where to store the items found.
    :return: nothing.
    """
    fin = open(filename, 'rt')
    in_msgstr = False
    for line in fin:
        if in_msgstr:
            if line[0] == '"':  # still inside a msgstr
                line_search(line, prefix, sc_set)
            else:
                in_msgstr = False  # not anymore in a msgstr
        else:
            if line[:6] == 'msgstr':  # entering a msgstr
                in_msgstr = True
                line_search(line, prefix, sc_set)
    fin.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
elif len(sys.argv) != 2:
    print("""\nUsage: list_tr_shortcuts.py <LANGUAGE>

    Examples: list_tr_shortcuts.py es
              list_tr_shortcuts.py fr\n""")
elif not os.path.isdir(os.path.join(root_path, 'locale', sys.argv[1])):
    print("'<repo_root>/locale/" + sys.argv[1] + "' folder not found.")
else:  # All OK
    kbdset = set()
    menuset = set()
    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'locale', sys.argv[1], 'LC_MESSAGES')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-3:] == '.po':
                file_process(path_full, ':kbd:', kbdset)
                file_process(path_full, ':menuselection:', menuset)

    print(':kbd: items:')
    k = sorted(kbdset)
    for item in k:
        print(item)
    m = sorted(menuset)
    print('\n\n:menuselection: items:')
    for item in m:
        print(item)
