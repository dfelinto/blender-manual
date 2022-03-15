#!/usr/bin/env python3
# Apache License, Version 2.0

"""
Utility that takes a reference and returns a file:line:column.

Useful for editors/IDE's to be able to jump to the reference under the cursor.

Notes:

- This command will only ever write an absolute file:line:column to the stdout.
- Errors always output to the stderr and return exit code 1.
"""
import os
import re

RST_EXT = (".rst", ".txt")


def rst_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath.startswith("."):
            continue
        for filename in filenames:
            if filename.startswith("."):
                continue
            ext = os.path.splitext(filename)[1]
            if ext.lower() == ".rst":
                yield os.path.join(dirpath, filename)


def find_vcs_root(test, dirs=(".svn", ".git"), default=None):
    import os
    prev, test = None, os.path.abspath(test)
    while prev != test:
        if any(os.path.isdir(os.path.join(test, d)) for d in dirs):
            return test
        prev, test = test, os.path.abspath(os.path.join(test, os.pardir))
    return default


def find_rst_root(test, files=("index.rst", "index.txt", "contents.rst", "contents.txt"), default=None):
    import os
    prev, test = None, os.path.abspath(test)
    test_found = default
    while prev != test:
        if any(os.path.exists(os.path.join(test, fn)) for fn in files):
            test_found = test
        prev, test = test, os.path.abspath(os.path.join(test, os.pardir))
    return test_found


re_find_references = re.compile(r"(^[ \t]*\.\.\s+_)([a-zA-Z0-9_\-]+):", re.MULTILINE)


def find_references(fn, data, find_ref):
    """
    Use to find instances of the :ref: role.
    """
    for g in re_find_references.finditer(data):
        if g[2] == find_ref:
            start = g.start()
            return data.count('\n', 0, start), len(g[1])
    return None, None


def create_argparse():
    import argparse

    usage_text = __doc__

    parser = argparse.ArgumentParser(
        prog="rst_lookup_reference",
        description=usage_text,
    )

    parser.add_argument(
        "--path",
        dest="path",
        help=(
            "Path to operate use as a reference when finding the root. "
            "Typically the path of the file containing what you want to find is sufficient. "
            "Use the current working directory when not passed."
        ),
    )

    parser.add_argument(
        "--find",
        dest="find",
        metavar='FIND',
        required=True,
        default=1, type=str,
        help=(
            "Text referring to a role, eg:\n"
            "  :ref:`My Reference <some-reference>`"
            "  :doc:`My Doc </path/to/document>`"
        ),
    )

    return parser


def main(argv=None):

    import sys
    import os
    import re

    if argv is None:
        argv = sys.argv[1:]

    parser = create_argparse()
    args = parser.parse_args(argv)

    # rst_root = find_vcs_root(args.path)
    rst_path = args.path or os.getcwd()
    if os.path.isdir(rst_path):
        rst_cwd = rst_path
    else:
        rst_cwd = os.path.dirname(rst_path)
    rst_cwd = os.path.abspath(rst_cwd)
    rst_root = find_rst_root(rst_cwd)
    if not rst_root:
        return

    re_role_match_brackets = r":([a-zA-Z0-9_]+):`[^<]*<([^>]+)>`"
    re_role_match = r":([a-zA-Z0-9_]+):`([^`]+)`"
    match = re.match(re_role_match_brackets, args.find)
    if match is None:
        match = re.match(re_role_match, args.find)

    if match is None:
        print("Could not match:", re_role_match, file=sys.stderr)
        sys.exit(1)

    role_id, role_data = match.groups()
    del match

    line = col = None
    if role_id == "ref":
        for fn in rst_files(rst_root):
            if os.path.exists(fn):
                with open(fn, 'r', encoding='utf-8') as f_handle:
                    data = f_handle.read()
                    line, col = find_references(fn, data, role_data)
                    if line is not None:
                        break
        if line is None:
            print("Could not find reference:", repr(role_data), "in", repr(rst_root), file=sys.stderr)
            sys.exit(1)

    elif role_id == "doc":
        if role_data.startswith("/"):
            # Absolute path.
            fn_noext = os.path.join(rst_root, role_data[1:])
        else:
            # Relative path.
            fn_noext = os.path.join(rst_cwd, role_data)

        fn = None
        fn_attempts = []
        for ext in RST_EXT:
            fn_test = fn_noext + ext
            if os.path.exists(fn_test):
                fn = fn_test
                break
            fn_attempts.append(fn_test)

        if fn is None:
            print("Could not find files:", repr(fn_attempts), file=sys.stderr)
            sys.exit(1)

        line = 1
        col = 0
    else:
        # TODO:
        # - term
        print("Role", role_id, "not handled!", file=sys.stderr)
        sys.exit(1)

    assert(line is not None)
    print("%s:%d:%d" % (fn, line, col))


if __name__ == "__main__":
    main()
