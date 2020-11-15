#! /usr/bin/env python3

# Checks that all the tables in the folder are consistent. Errors checked:
#     * Duplicated input names
#     * Duplicated output names (not tested by default)
#     * Input names containing other input names in the wrong order

import os

test_dup_outputs = False  # set to True to check for duplicated output names


def chk_indup(tbl):
    result = True
    t = [i[0] for i in tbl]
    for i in t:
        if t.count(i) > 1:
            print(f"    Input value '{i}' appears {t.count(i)} times.")
            while i in t:
                t.remove(i)
            result = False
    return result


def chk_outdup(tbl):
    result = True
    if test_dup_outputs:
        t = [i[1] for i in tbl]
        for i in t:
            if t.count(i) > 1:
                print(f"    Output value '{i}' appears {t.count(i)} times.")
                while i in t:
                    t.remove(i)
                result = False
    return result


def chk_subs(tbl):
    result = True
    t = [i[0] for i in tbl]
    while len(t) > 0:
        item = t.pop(0)
        for i in t:
            if item in i and len(item) < len(i):
                print(f"    Input name '{item}' is included in later '{i}'.")
                result = False
    return result


files = os.listdir(os.path.dirname(__file__))
for filename in files:
    if filename[0:5] == 'table' and filename[-4:] == '.csv':
        print("Checking '" + filename + "'...")
        table = []
        f = open(filename, 'rt')
        for ln in f:
            row = ln.strip()
            if row != '' and row[0] != '#':
                r = row.split(';')
                table.append((r[0].strip(), r[1].strip()))
        f.close()
        c1 = chk_indup(table)
        c2 = chk_outdup(table)
        c3 = chk_subs(table)
        if c1 and c2 and c3:
            print(' OK.')
        print()
