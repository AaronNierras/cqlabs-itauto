#!/usr/bin/env python3

import os
import requests


# info
src = "./supplier-data/descriptions/"
url = "http://34.75.49.83/fruits/"


def get_desc(src_path):
    paragraph = []
    for infile in os.listdir(src_path):
        src_file = os.path.join(src_path, infile)
        try:
            with open(src_file) as f:
                lines = f.readlines()
                desc = "name: {},weight: {}".format(lines[0].strip(), lines[1].strip())
                paragraph.append(desc)
        except FileNotFoundError:
            print(">>> File '{}' not found.".format(src_file))

    return paragraph

def upload_desc(src_path, url):
    for infile in os.listdir(src_path):
        file, _ = os.path.splitext(infile)
        src_file = os.path.join(src_path, infile)
        try:
            with open(src_file) as f:
                lines = f.readlines()
                desc = {
                    "name": lines[0].strip(),
                    "weight": int(lines[1].strip().split(" ")[0]),
                    "description": ''.join(lines[2:]).strip(),
                    "image_name": "".join([file, ".jpeg"])
                }
                r = requests.post(url, json=desc)
            print(">>> File '{}' uploaded. (response:{})".format(src_file, r.status_code))
        except FileNotFoundError:
            print(">>> File '{}' not found.".format(src_file))

if __name__ == "__main__":
	upload_desc(src, url)
