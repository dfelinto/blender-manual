#! /usr/bin/env python3

# Shows a list of all the :kbd: and :menuselection: items present in the
# RST files in the repository.

import os

kbdset = set()
menuset = set()


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


def line_search(line, prefix, itemset):
    """
    It searches a line from the RST file.
    :param line: the line from the RST file.
    :param prefix: type of element (:kbd:, :menuselection:,...).
    :param itemset: the set where to add the found elements.
    :return: nothing.
    """
    lin = line
    while True:
        # shortcut start search
        pos = lin.find(prefix + '`')
        if pos == -1:
            break
        lin = lin[pos+len(prefix)+1:]

        # shortcut end search
        pos = lin.find('`')  # we assume it will be found
        s_in = lin[:pos]  # string to add to the set
        itemset.add(s_in)
        lin = lin[pos:]


def file_process(filename):
    """
    It processes the RST file searching for items.
    :param filename: the name of the RST file.
    :return: nothing.
    """
    global kbdset
    global menuset
    fin = open(filename, 'rt')
    for line in fin:
        line_search(line, ':kbd:', kbdset)  # :kbd: shortcuts
        line_search(line, ':menuselection:', menuset)  # :menuitem: menu items
    fin.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
else:  # All OK
    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'manual')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-4:] == '.rst':
                file_process(path_full)

    print(':kbd: items:')
    k = sorted(kbdset)
    for item in k:
        print(item)
    m = sorted(menuset)
    print('\n\n:menuitem: items:')
    for item in m:
        print(item)
