#! /usr/bin/env python3

# Changes the shortcuts (:kbd:`...`) across all the manual RST
# files according to the provided CSV table.

import os

n_changes = 0
table = []


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
    global table
    result = s
    for entry in table:
        result = result.replace(entry[0], entry[1])
    return result


def line_process(line):
    """
    It processes a line from the RST file.
    :param line: the line from the RST file.
    :return: the processed (replaced) line.
    """
    result = ''
    lin = line
    global n_changes
    while True:
        # shortcut start search
        pos = lin.find(':kbd:`')
        if pos == -1:
            result += lin
            break
        result += lin[:pos+6]
        lin = lin[pos+6:]

        # shortcut end search
        pos = lin.find('`')  # we assume it will be found
        s_in = lin[:pos]  # candidate shortcut string to suffer replacements
        s_out = st_replace(s_in)
        result += s_out
        lin = lin[pos:]
        if s_in != s_out:
            n_changes += 1
    return result


def file_process(filename):
    """
    It processes the RST file to replace and generates the output file
    if needed.
    :param filename: the name of the RST file.
    :return: nothing.
    """
    fin = open(filename, 'rt')
    fout_list = []
    global n_changes
    n_changes = 0
    for line in fin:
        lin = line_process(line)
        fout_list.append(lin)
    fin.close()

    # In case there were changes, we generate an output file
    if n_changes > 0:
        print(filename[filename.find('manual')+6:] + ':',
              n_changes, "change(s).")
        file_out = 'new_' + filename[filename.find('manual'):]
        os.makedirs(os.path.dirname(file_out), exist_ok=True)
        fout = open(file_out, 'wt')
        fout.writelines(fout_list)
        fout.close()


root_path = find_vcs_root()

# Preliminary checks:
if root_path is None:
    print('Repository not found. Script must be in a repo subfolder.')
elif not os.path.isfile('table.csv'):
    print("'table.csv' file not found. "
          "Script and 'table.csv' must be in the same folder.")
else:  # All OK
    # Substitution table initialization:
    f = open('table.csv', 'rt')
    for ln in f:
        row = ln.strip()
        if row != '':
            table.append(row.split(';'))
    f.close()

    # Main loop:
    for info_dir in os.walk(os.path.join(root_path, 'manual')):
        for fname in info_dir[2]:
            path_full = os.path.join(info_dir[0], fname)
            if path_full[-4:] == '.rst':
                file_process(path_full)
