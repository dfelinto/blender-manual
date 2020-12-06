#!/usr/bin/env python3
# Apache License, Version 2.0

# This script is to reduce tedious steps involved when updating PO files
# for multiple languages.
# It looks more complex then it really is, since we do multi-processing
# to update the PO files, to save some time.

# Subversion Checkout Location
# ============================
#
# Note: this script supports subversion repositories at these locations:
#
# ./local/(.svn)          All languages in one checkout.
# ./local/{LANG}/(.svn)   Each language in it's own checkout.
#
# All commands run from the project root, passing in paths
# without changing directories.
#
# This works since subversion will detect the parent directories ".svn"
# path without us having to change directories.

import os
import sys
import shutil
import subprocess
import multiprocessing
from shlex import quote
import re

import importlib.util
mod_file_path = os.path.join(os.path.dirname(__file__), "..", "tools_rst", "rst_check_locale.py")
spec = importlib.util.spec_from_file_location("rst_check_locale", mod_file_path)
rst_check_locale = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rst_check_locale)


VERBOSE = False
USE_MULTI_PROCESS = True


def run_svn(args, with_output=False):
    cmd = ["svn", *args]
    if VERBOSE:
        print(">>> ", cmd)

    if not with_output:
        subprocess.check_call(
            cmd,
        )
    else:
        return subprocess.check_output(
            cmd,
        )


def run_multiprocess__single(arg_list):
    return_codes = [None] * len(arg_list)
     # Single process.
    for args_index, args in enumerate(arg_list):
        proc = subprocess.Popen(["sphinx-intl", *args])
        proc.wait()
        return_codes[args_index] = proc.returncode

    return return_codes


def run_multiprocess__multi(arg_list, job_total=1):
    return_codes = [None] * len(arg_list)

    # Real multi-processing.
    import time
    processes = []

    def processes_clear_finished():
        for proc_index in reversed(range(len(processes))):
            proc_cmd_index, proc = processes[proc_index]
            if proc.poll() is not None:
                del processes[proc_index]
                return_codes[proc_cmd_index] = proc.returncode

    for args_index, args in enumerate(arg_list):
        while True:
            processes_clear_finished()
            if len(processes) <= job_total:
                break
            else:
                time.sleep(0.1)

        sys.stdout.flush()
        sys.stderr.flush()

        processes.append((args_index, subprocess.Popen(["sphinx-intl", *args])))

    while processes:
        processes_clear_finished()
        time.sleep(0.1)

    return return_codes


def run_multiprocess(arg_list, job_total=1):
    if job_total <= 1:
        return run_multiprocess__single(arg_list)
    else:
        return run_multiprocess__multi(arg_list, job_total)


# -----------------------------------------------------------------------------
# Setup Global State


if USE_MULTI_PROCESS:
    CPU_COUNT = multiprocessing.cpu_count()
else:
    CPU_COUNT = 1

# Python needs utf-8.
os.environ["LANG"] = "en_US.UTF-8"

# Ensure we're in the repo's base:
ROOT_DIR = os.path.normpath(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))
os.chdir(ROOT_DIR)
LOCALE_BUILD_DIR = os.path.join(ROOT_DIR, "build", "gettext")

LOCALE_DIR = os.path.join(ROOT_DIR, "locale")

# When we cannot use portable API's.
IS_WIN32 = (os.name == "nt")


# -----------------------------------------------------------------------------
# Main Function

def main():

    # True when all languages are checked out under "locale/".
    has_complete_locale_checkout = os.path.exists(os.path.join(LOCALE_DIR, ".svn"))

    # All directories containing '.svn' (the parent directory).
    svn_dirs_all = []
    for svn_dir in os.listdir(LOCALE_DIR):
        if not svn_dir in ("weblate", "sphinx"):
            if not svn_dir.startswith((".", "_")):
                svn_dir = os.path.join(LOCALE_DIR, svn_dir)
                if os.path.isdir(svn_dir):
                    svn_dirs_all.append(svn_dir)
    # Only for reproducible execution.
    svn_dirs_all.sort()

    # ---------------------
    # Update the Locale Dir
    #
    # It's easy to accidentally have a repository in an invalid state,
    # and it's not always obvious that this is the cause of failure to commit.
    # Play it safe and cleanup every time.

    if has_complete_locale_checkout:
        run_svn(["cleanup", LOCALE_DIR])
        run_svn(["up", LOCALE_DIR])
    else:
        for svn_dir in svn_dirs_all:
            run_svn(["cleanup", svn_dir])
            run_svn(["up", svn_dir])

    # ---------------
    # Create PO Files

    if os.path.exists(LOCALE_BUILD_DIR):
        shutil.rmtree(LOCALE_BUILD_DIR)

    # Same as 'make gettext'.
    subprocess.check_call([
        "sphinx-build",
        "-t", "builder_html",
        "-b", "gettext",
        "-j", str(CPU_COUNT),
        # Source.
        "manual",
        # Destination.
        LOCALE_BUILD_DIR,
    ])

    # ---------------
    # Update PO Files
    #
    # Note, this can be slow so (multi-process).

    po_lang_all = []
    for po_lang in os.listdir(LOCALE_DIR):
        if not svn_dir in ("weblate", "sphinx"):
            if (not po_lang.startswith((".", "_")) and
                    os.path.isdir(os.path.join(LOCALE_DIR, po_lang))):
                po_lang_all.append(po_lang)
    # Only for reproducible execution.
    po_lang_all.sort()

    sphinx_intl_arg_list = []
    for po_lang in po_lang_all:
        sphinx_intl_arg_list.append([
            "--config=" + os.path.join("manual", "conf.py"),
            "update",
            "--pot-dir=" + LOCALE_BUILD_DIR,
            "--language=" + po_lang,
        ])

    sphinx_intl_return_codes = run_multiprocess(
        sphinx_intl_arg_list,
        job_total=CPU_COUNT,
    )

    if set(sphinx_intl_return_codes) - {0}:
        print("Warning, the following commands returned non-zero exit codes:")
        for returncode, arg in zip(sphinx_intl_return_codes, sphinx_intl_arg_list):
            if returncode != 0:
                print("returncode:", returncode, "from command:", "sphinx-intl", arg)
        print("Some manual corrections might need to be done.")
    del sphinx_intl_return_codes, sphinx_intl_arg_list


    # ----------
    # Handle SVN

    # Add newly created PO files:
    for svn_dir in svn_dirs_all:
        # Multiple args, don't quote.
        svn_files_new = []
        svn_dirs_new = []
        for line in run_svn(("status", svn_dir), True).decode("utf-8").splitlines():
            if line.startswith("?"):
                line = line.strip()
                line = line.split()[-1]
                if line.endswith(".po"):
                    svn_files_new.append(line)
                elif os.path.isdir(line):
                    svn_dirs_new.append(line)

        if svn_files_new:
            run_svn(["add", *svn_files_new, *svn_dirs_new])
        del svn_files_new, svn_dirs_new

    # Notify on redundant PO files.
    try:
        rst_check_locale.warn_locale()
    except:
        print("rst_check_locale.py has no warn_locale function")

    # ---------------------
    # Print Commit Messages
    #
    # Use space prefix as shell's (bash/zsh/fish) uses this as a hint not to store in the users history.
    revision = re.findall(
        r"^Revision:\s([\d]+)",
        run_svn(["info", ROOT_DIR], True).decode('utf8'),
        flags=re.MULTILINE,
    )
    revision = revision[0] if revision else "Unknown"

    # Note that when 'has_complete_locale_checkout == True' we _could_ commit all languages at once,
    # however this can cause commits that are so large, they take a long time and risk hanging.
    # So commit every language on it's own.

    for svn_dir in svn_dirs_all:
        # 'shlex.quote' causes path separator to be converted to forward slashes,
        # causing the command to fail.
        if IS_WIN32:
            print("  " + subprocess.list2cmdline(["svn", "ci", svn_dir, "-m", "Update r" + revision]))
        else:
            print("  svn ci {:s} -m \"Update r{:s}\"".format(quote(svn_dir), revision))

if __name__ == "__main__":
    main()
