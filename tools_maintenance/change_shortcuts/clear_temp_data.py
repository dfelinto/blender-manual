#! /usr/bin/env python3

# Deletes all temp files and directories (if they exist):
#     * 'new_locale' subfolder.
#     * 'new_manual' subfolder.
#     * All diff files.

import os
import shutil
import glob


shutil.rmtree('new_locale', ignore_errors=True)
shutil.rmtree('new_manual', ignore_errors=True)
for file in glob.glob('diff*.txt'):
    os.remove(file)
