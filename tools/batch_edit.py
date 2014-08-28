#!/usr/bin/env python3

import os
# if you want to operate on a subdir, eg: "render"
SUBDIR = ""
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
RST_DIR = os.path.normpath(os.path.join(CURRENT_DIR, "..", "manual", SUBDIR))


def rst_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath.startswith("."):
            continue

        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext.lower() == ".rst":
                yield os.path.join(dirpath, filename)


def main():
    for fn in rst_files(RST_DIR):
        with open(fn, "r", encoding="utf-8") as f:
            data_src = f.read()
            data_dst = operation(fn, data_src)

        if data_dst is None or (data_src == data_dst):
            continue

        with open(fn, "w", encoding="utf-8") as f:
            data_src = f.write(data_dst)


# ---------------------------------------
# Custom Code - do whatever you like here
# (only commit reusable examples).
#
# Functions take a (file_name, file_contents)
# returns the new file_contents (or None to skip the operation)


def strip_trailing_space(fn, data_src):
    """
    Strips trailing whitespace
    """

    lines = data_src.split("\n")

    for i, l in enumerate(lines):
        l = l.rstrip()
        lines[i] = l

    data_dst = "\n".join(lines)
    return data_dst


def warn_long_lines(fn, data_src):
    """
    Complain about long lines
    """
    lines = data_src.split("\n")
    limit = 118

    for i, l in enumerate(lines):
        if len(l) > limit:
            print("%s:%d: long line %d" % (fn, i + 1, len(l)))

        l = l.rstrip()

    return None


def edit_directive_body(fn, data_src):
    """
    Replaces
       :doc:`Some Page </path/to/rst_file>`
    Or
       :doc:`/path/to/rst_file`
    """

    # may want to use other directives which have similar syntax
    directive = ":doc:"
    def handle_directive(d):
        """
        Takes and returns a directives content (do whatever you need here)
        """
        # ensure absolute paths
        #if d[0] != "/":
        #    return "/" + d
        return d

    lines = data_src.split("\n")

    for i, l in enumerate(lines):
        # position in line
        p = 0
        while True:
            # Could use regex magic here, but for now use simple string manipulation
            p_find = l.find(directive + "`", p)
            if p_find == -1:
                break

            p_end = l.find("`", p_find + len(directive) + 1)
            if p_end == -1:
                raise Exception("%s:%d: Unmatched reference found!" % (fn, i + 1))
            p_end += 1

            # print(l[p_find:p_end])
            if "<" in l[p_find:p_end]:
                # handle:
                #   :doc:`Some Page </path/to/rst_file>`
                p_body_start = l.find("<", p_find, p_end)
                p_body_end = l.find(">", p_body_start, p_end)
                assert(p_body_start != -1)
                assert(p_body_end != -1)
                p_body_start += 1
                p_end += 1
            else:
                # handle:
                #   :doc:`/path/to/rst_file`
                p_body_start = p_find + len(directive) + 1
                p_body_end = p_end - 1

            # directive is:
            d_src = l[p_body_start:p_body_end]
            if not d_src.strip():
                raise Exception("%s:%d: Empty reference found!" % (fn, i + 1))
            d_dst = handle_directive(d_src)

            l = l[:p_body_start] + d_dst + l[p_body_end:]

            p_end += len(d_dst) - len(d_src)

            p = p_end

        lines[i] = l

    data_dst = "\n".join(lines)
    return data_dst


# define the operation to call
operation = strip_trailing_space


if __name__ == "__main__":
    main()
