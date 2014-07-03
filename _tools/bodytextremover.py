#!/usr/bin/env python3

import os

def source_list(path, filename_check=None):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename_check is None or filename_check(filename):
                yield os.path.join(dirpath, filename)

CWD = "../"

images = set()
for f in source_list(CWD, filename_check=lambda f: f.endswith(".rst")):
    if not ("index.rst" in f or "contents.rst" in f):
        print(f)
        fa = open(f, "r+", encoding="utf-8")
        lines = fa.readlines()
        fa.write( ''.join( lines[:8] ) )
        fa.close()
