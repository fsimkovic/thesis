#!/usr/bin/env python

import argparse
import re

RE_KEY = re.compile("^@[A-Za-z]+{(.*),$")
RE_CITE = re.compile("\\cite{.*}")


class Entry(object):

    def __init__(self):
        self.key = None
        self.text = ""

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.key)


def read_bib(f):
    entries = {}
    with open(f, "r") as f_in:
        lines = iter(f_in.readlines())
        line = next(lines)
        while True:
            if RE_KEY.match(line.strip()):
                e = Entry()
                e.key = RE_KEY.match(line.strip()).groups(1)[0]
                while True:
                    e.text += line
                    line = next(lines)
                    if line.strip() == "}":
                        e.text += line
                        break
                assert e.key not in entries
                entries[e.key] = e
            try:
                line = next(lines)
            except StopIteration:
                break
    return entries


def read_tex(f):
    keys = set()
    with open(f, "r") as f_in:
        for line in f_in:
            for word in line.strip().split():
                if RE_CITE.search(word):
                    keys.update(set(word.split("{")[1].split("}")[0].split(",")))
                if "textcite" in word:
                    keys.update(set(word.split("{")[1].split("}")[0].split(",")))

    return keys


def write_bib(f, bib_entries, tex_keys):
    with open(f, "w") as f_out:
        for key in sorted(tex_keys):
            f_out.write(bib_entries[key].text)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("bibliography")
    p.add_argument("texfiles", nargs="+")
    args = p.parse_args()

    bib_entries = read_bib(args.bibliography)    
    tex_keys = set()
    for tex in args.texfiles:
        tex_keys.update(read_tex(tex))
    
    write_bib("test.bib", bib_entries, tex_keys)
