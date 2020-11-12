#!/usr/bin/env python3

"""
Utility to open an warning/error reports in an editor, a list of locations:

/path/file.ext:line:col:
"""

import sys
import shutil
import subprocess


def run(cmd):
    proc = subprocess.Popen(cmd, shell=False)
    proc.wait()
    return proc.returncode


logfile = sys.argv[-1]

if shutil.which("emacsclient"):
    sys.exit(run((
        "emacsclient",
        "--eval",
        # Calling: (compile-goto-error) should work but doesn't open window when called from here.

        "(progn "
        "  (find-file " f"\"{logfile}\")"
        "  (compilation-mode)"
        # To to the last non-blank line.
        "  (goto-char (point-max))"
        "  (skip-chars-backward \"\n[:space:]\")"
        "  (move-beginning-of-line nil)"
        ")",
        "--no-wait",
        "--alternate-editor=emacs --eval",
    )))

elif shutil.which("gvim"):
    sys.exit(run((
        "gvim",
        "--nofork",
        "-c",
        "cfile rst_check_syntax.log",
        "-c"
        "cope",
        "-c",
        "clast",
    )))
else:
    print("Error, no editor found (emacsclient, gvim)")
    sys.exit(1)
