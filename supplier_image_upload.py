#!/usr/bin/env python3

import os
import requests


# info
src = "~/supplier-data/images"
url = "http://localhost/upload/"


def upload(src_path, url):
    for infile in os.listdir(src_path):
        src_file = os.path.join(src_path, infile)
        try:
            with open(src_file, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
            print(">>> File '{}' uploaded. (response:{})".format(src_file, r.status_code))
        except FileNotFoundError:
            print(">>> File '{}' not found.".format(src_file))



if __name__ == "__main__":
	upload(src, url)
