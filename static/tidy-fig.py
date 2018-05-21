#!/usr/bin/env python3

import argparse
import glob2
import os
import re

RE_IGRAPHICS = re.compile("^\\\includegraphics\[.*\]{(.*)}$")


class Figure(object):
    def __init__(self):
        self.key = None
        self.value = None

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.value)


def read_tex(f):
    keys = set()
    with open(f, "r") as f_in:
        for line in f_in:
            for word in line.strip().split():
                if RE_IGRAPHICS.match(word.strip()):
                    keys.add(RE_IGRAPHICS.match(word.strip()).group(1))
    return keys


def find_img(d, ext=['png', 'pdf', 'jpg', 'svg']):
    for e in ext:
        for img in glob2.glob(os.path.join(d, '**', '*.' + e)):
            if 'originals' in img:
                continue
            figure = Figure()
            figure.key = os.path.basename(img)
            figure.value = img
            yield figure


def print_diff(tex_keys, images):
    for img in images:
        if img.key in tex_keys:
            tex_keys.remove(img.key)
        else:
            print(">>>", img.key)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("imagesd")
    p.add_argument("texfiles", nargs="+")
    args = p.parse_args()

    images = list(find_img(args.imagesd))

    tex_keys = set()
    for tex in args.texfiles:
        tex_keys.update(read_tex(tex))

    print_diff(tex_keys, images)
