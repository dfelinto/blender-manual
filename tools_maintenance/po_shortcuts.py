#! /usr/bin/env python3

"""
Changes the shortcuts (:kbd:`...`) across all the translated PO files
of a specific language, according to the provided JSON table.
Language code must be provided.
"""

import sys
import os
import re
import json

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PO_DIR = os.path.normpath(os.path.join(CURRENT_DIR, "..", "locale"))

ROLE = 'kbd'  # Change to any other role if needed


def po_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        if dirpath.startswith("."):
            continue
        for filename in filenames:
            if filename.startswith("."):
                continue
            ext = os.path.splitext(filename)[1]
            if ext.lower() == ".po":
                yield os.path.join(dirpath, filename)


def parse_po(text):
    """
    Parse the given po text for msgstrs.

    :param text: the text of the po file.
    :yield: text of the msgstr, start char position.
    """
    msgstr = []
    pos = 0
    for line in text.splitlines(keepends=True):
        if msgstr:
            if line.startswith('"'):
                msgstr.append(line)
            else:
                yield "".join(msgstr), start
                msgstr = []
        else:
            if line.startswith('msgstr'):
                msgstr.append(line)
                start = pos

        pos += len(line)

    if msgstr:
        yield "".join(msgstr), start


def read_json(lang):
    def parse_json(obj):
        """
        Function used to parse the json file. Find table and search for duplicates.

        :param obj: tuple passed by 'json.load()'.
        :return: if 'obj' is top level, it returns the table in a list of 2-tuples,
                 or None if table not found, or duplicate elements present.
                 If not on top level, it just returns the passed object.
        """
        retval = obj
        if isinstance(obj[0][1], list):  # top level?
            retval = None  # language table not found so far
            for tpl in obj:
                if tpl[0] == lang:  # table found?
                    retval = tpl[1]
                    break
            if retval:  # table was found?
                # Check for duplicates:
                test_set = set(entry[0] for entry in retval)
                if len(test_set) < len(retval):  # duplicates?
                    raise ValueError("table contains duplicate entries")
            else:
                raise ValueError("table not found")
        return retval

    filename = 'po_shortcuts_tables.json'
    try:
        with open(filename, 'r', encoding="utf-8") as json_file:
            table = json.load(json_file, object_pairs_hook=parse_json)

    except (IOError, OSError) as err:
        print("{0}: cannot read data file: {1}".format(filename, err))
        return None

    except json.JSONDecodeError as err:
        print("{0}: cannot decode data file: {1}".format(filename, err))
        return None

    except ValueError as err:
        print("{0}: {1}".format(filename, err))
        return None

    return table


def main(lang):
    # todo all available langs for admins

    lang_dir = os.path.join(PO_DIR, lang)
    if not os.path.exists(lang_dir):
        print("Language folder not found:", lang)
        return

    table = read_json(lang)
    if not table:
        return

    table_compiled = []
    for key, value in table:
        pattern_str = r'(\:' + ROLE + \
            r'\:["\s]*?`[^`]*?)\b' + key + r'\b([^`]*?`)'
        replace = r'\1' + value + r'\2'
        table_compiled.append((re.compile(pattern_str, re.MULTILINE),
                               replace))

    for filename in po_files(lang_dir):
        with open(filename, 'r', encoding="utf-8") as f:
            text_src = f.read()

        text_dst = []
        last_end = 0
        n_total = 0
        for msgstr, start in parse_po(text_src):
            text_dst.append(text_src[last_end:start])
            last_end = start + len(msgstr)

            for pattern, repl in table_compiled:
                msgstr, n = re.subn(pattern, repl, msgstr)
                n_total += n

            text_dst.append(msgstr)

        if n_total != 0:
            if last_end != len(text_src):
                text_dst.append(text_src[last_end:])

            with open(filename, 'w', encoding="utf-8") as f:
                f.write("".join(text_dst))

            print(filename[filename.find('LC_MESSAGES')+11:] +
                  ':', n_total, 'change(s).')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage: {0} <LANGUAGE>\nExamples: {0} es"
              .format(os.path.basename(__file__)))
    else:
        main(sys.argv[1])
