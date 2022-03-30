#!/usr/bin/env python3
# Apache License, Version 2.0
# <pep8 compliant>

"""
General purpose tool for remapping directory structure of RestructuredText documents.

This tool allows you to snapshot the structure, move files and directories about,
then finish the operation and all :doc:`... </path/to/file>` roles will be updated automatically.

Usage:

 1) rst_remap.py start
 2) # Reorganize the document structure, rename files.
 3) rst_remap.py finish

note: you can't change the contents of the files you are remapping.
"""

import sys
import os


# -----------------------------------------------------------------------------
# Generic Functions

def uuid_from_file(fn, block_size=1 << 20):
    """
    Returns an arbitrary sized unique ASCII string based on the file contents.
    (exact hashing method may change).
    """
    with open(fn, 'rb') as f:
        # first get the size
        import os
        f.seek(0, os.SEEK_END)
        size = f.tell()
        f.seek(0, os.SEEK_SET)
        del os
        # done!

        import hashlib
        sha1 = hashlib.new('sha512')
        while True:
            data = f.read(block_size)
            if not data:
                break
            sha1.update(data)
        # skip the '0x'
        return hex(size)[2:] + sha1.hexdigest()


# -----------------------------------------------------------------------------
# Command Line Interface


def fatal(msg):
    if __name__ == "__main__":
        sys.stderr.write("fatal: ")
        sys.stderr.write(msg)
        sys.stderr.write("\n")
        sys.exit(1)
    else:
        raise RuntimeError(msg)


# if you want to operate on a subdir, e.g: "render"
SUBDIR = ""
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
RST_DIR = os.path.normpath(os.path.join(CURRENT_DIR, "..", "manual", SUBDIR))

# name for temp file
RST_MAP_ID = "rst_map.data"


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


def image_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath.startswith("."):
            continue

        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext.lower() in {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"}:
                yield os.path.join(dirpath, filename)


def remap_data_create(base_path):

    if os.sep != "/":
        def compat_path(fn):
            return "/" + fn.replace("\\", "/")
    else:
        def compat_path(fn):
            return "/" + fn

    # store rst's without extension
    remap_rst = {}
    for fn in rst_files(base_path):
        file_hash = uuid_from_file(fn)
        file_path = compat_path(os.path.splitext(
            os.path.relpath(fn, base_path))[0])
        file_path_prev = remap_rst.get(file_hash)
        if file_path_prev is not None:
            print("Duplicate file contents: %r, %r" %
                  (file_path_prev, file_path))
        else:
            remap_rst[file_hash] = file_path

    # images keep their extension
    remap_images = {}
    for fn in image_files(base_path):
        file_hash = uuid_from_file(fn)
        file_path = compat_path(os.path.relpath(fn, base_path))
        file_path_prev = remap_images.get(file_hash)
        if file_path_prev is not None:
            print("Duplicate file contents: %r, %r" %
                  (file_path_prev, file_path))
        else:
            remap_images[file_hash] = file_path

    return (remap_rst, remap_images)


def remap_start(base_path):
    filepath_remap = os.path.join(base_path, RST_MAP_ID)

    if os.path.exists(filepath_remap):
        fatal("Remap in progress, run with 'finish' or remove %r" %
              filepath_remap)

    remap_data_src = remap_data_create(base_path)

    with open(filepath_remap, 'wb') as fh:
        import pickle
        pickle.dump(remap_data_src, fh, pickle.HIGHEST_PROTOCOL)
    print("Remap started, tracking (%d rst, %d image) files." %
          (len(remap_data_src[0]), len(remap_data_src[1])))


def remap_finish(base_path):
    filepath_remap = os.path.join(base_path, RST_MAP_ID)

    if not os.path.exists(filepath_remap):
        fatal("Remap not started, run with 'start', (%r not found)" %
              filepath_remap)

    with open(filepath_remap, 'rb') as fh:
        import pickle
        remap_data_src = pickle.load(fh)

    remap_data_dst = remap_data_create(base_path)

    remap_rst_src, remap_image_src = remap_data_src
    remap_rst_dst, remap_image_dst = remap_data_dst

    remap_finish_rst(base_path, remap_rst_src, remap_rst_dst)
    remap_finish_image(base_path, remap_image_src, remap_image_dst)

    os.remove(filepath_remap)


def _src_dst_map(remap_src, remap_dst):
    # Store: {source: dest}, without path prefix or extension, e.g:
    # /path/to/docs/manual/interface/introduction.rst, becomes...
    #                     /interface/introduction
    src_dst_map = {}

    for file_hash, file_path_src in remap_src.items():
        file_path_dst = remap_dst.get(file_hash)
        if file_path_dst is None:
            # shouldn't happen often.
            print("warning: source '%s' not found!" % file_path_src[1:])
            file_path_dst = file_path_src

        src_dst_map[file_path_src] = file_path_dst
        if file_path_src.endswith("/index") and file_path_src != "/index":
            src_dst_map[file_path_src[:-6]] = file_path_dst[:-6]

    return src_dst_map


def remap_finish_rst(base_path, remap_rst_src, remap_rst_dst):
    src_dst_map = _src_dst_map(remap_rst_src, remap_rst_dst)

    # now remap the doc links
    import rst_helpers

    for fn in rst_files(base_path):
        for d in rst_helpers.role_iter(fn, "doc", angle_brackets=True):
            file_rstpath_src = d[-2].strip()
            if "#" in file_rstpath_src:
                file_rstpath_src, tail = file_rstpath_src.split("#", 1)
            else:
                tail = None

            file_rstpath_dst = src_dst_map.get(file_rstpath_src)
            if file_rstpath_dst is not None:
                if tail is not None:
                    file_rstpath_dst = file_rstpath_dst + "#" + tail
                d[-2] = file_rstpath_dst
            else:
                print("warning: unknown path %r" % file_rstpath_src)


def remap_finish_image(base_path, remap_image_src, remap_image_dst):
    src_dst_map = _src_dst_map(remap_image_src, remap_image_dst)

    # now remap the doc links
    import rst_helpers
    from itertools import chain

    for fn in rst_files(base_path):
        for d in chain(rst_helpers.directive_iter(fn, "figure"),
                       rst_helpers.directive_iter(fn, "image")):
            file_imagepath_src = d[-1].strip()

            file_imagepath_dst = src_dst_map.get(file_imagepath_src)
            if file_imagepath_dst is not None:
                d[-1] = file_imagepath_dst
            else:
                print("warning: unknown path %r" % file_imagepath_src)


def main(argv=sys.argv):
    base_path = RST_DIR

    if "start" in argv:
        remap_start(base_path)
    elif "finish" in argv:
        remap_finish(base_path)
    else:
        print(__doc__)
        print("Pass either 'start' or 'finish' as arguments")


if __name__ == "__main__":
    main()
