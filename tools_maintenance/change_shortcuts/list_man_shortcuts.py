#! /usr/bin/env python3

# Shows a list of all the :kbd: and :menuselection: items present in the
# RST files in the repository.

import os


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


def file_process(filename, prefix, sc_set):
    """
    It processes the RST file searching for items with the given
    prefix; it adds them in the given set.
    :param filename: the name of the RST file.
    :param prefix: prefix to look for (':kbd:' or ':menuselect:').
    :param sc_set: set where to store the items found.
    :return: nothing.
    """
    fin = open(filename, 'rt')
    for line in fin:
        while True:
            # shortcut start search
            pos = line.find(prefix + '`')
            if pos == -1:
                break
            line = line[pos + len(prefix) + 1:]

            # shortcut end search
            pos = line.find('`')  # we assume it will be found
            s_in = line[:pos]  # string to add to the set
            sc_set.add(s_in)
            line = line[pos:]
    fin.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
else:  # All OK
    kbdset = set()
    menuset = set()
    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'manual')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-4:] == '.rst':
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
