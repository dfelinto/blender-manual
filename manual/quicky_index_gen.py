# Apache License, Version 2.0

"""
Script to create a partial index, for generating partial chapters.

Called from conf.py
"""

# Note, keep Python2 & 3 Compatible
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def from_chapters():
    """
    Return conf.py: (master_doc, exclude_patterns) values.
    """

    master_doc = "index"
    exclude_patterns = []

    quicky_chapters = [c for c in os.environ.get('QUICKY_CHAPTERS', "").strip(":").split(":") if c]
    if not quicky_chapters:
        return master_doc, exclude_patterns

    master_doc = "index_quicky"

    fn_src = os.path.join(CURRENT_DIR, "index.rst")
    fn_dst = os.path.join(CURRENT_DIR, "index_quicky.rst")

    f = open(fn_src, 'r', encoding="utf-8")
    data = f.read()
    f.close()
    del f

    lines = data.split("\n")

    lines_new = []
    for l in lines:
        l_orig = l

        # Extract the identifier
        # world/index.rst --> world
        # world.rst       --> world

        l = l.strip()
        if l.endswith(".rst"):
            l = l[:-4]
            if l.endswith("/index"):
                l = l.rsplit("/", 1)[0]
            # Now we have an identifier
            if l not in quicky_chapters:
                print("  skipping:", l_orig.strip())
                continue
            print("  using:", l_orig.strip())
        lines_new.append(l_orig)

    data = "\n".join(lines_new)

    f = open(fn_dst, 'w', encoding="utf-8")
    f.write(data)
    f.close()
    del f

    # now exclude all dirs not in chapters
    exclude_patterns.append("index.rst")
    for fn in os.listdir(CURRENT_DIR):
        if os.path.isdir(os.path.join(CURRENT_DIR, fn)):
            if fn not in quicky_chapters:
                print("  exclude:", fn)
                exclude_patterns.extend([
                        fn,
                        fn + ".rst",
                        ])

    return master_doc, exclude_patterns
