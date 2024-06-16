#!/usr/bin/env python3

from PIL import Image
import os

# info
src = "./supplier-data/images"
dst = src[:]
size = (600, 400)
ext = ".jpeg"


def convert(src_path):
    for infile in os.listdir(src_path):
        if infile in ["README", "LICENSE"]:
            continue
        file, _ = os.path.splitext(infile)
        src_file = os.path.join(src_path, infile)
        dst_file = os.path.join(src_path, "".join([file, ext]))
        if src_file == dst_file:
            continue
        try:
            with Image.open(src_file) as img:
                img = img.convert("RGB")
                img = img.resize(size)
                img.save(dst_file, format="JPEG")
            print(">>> Converted {}.".format(src_file))
        except FileNotFoundError:
            print(">>> File '{}' not found.".format(src_file))



if __name__ == "__main__":
	convert(src)
