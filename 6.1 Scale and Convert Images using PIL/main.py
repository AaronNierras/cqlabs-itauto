#!/usr/bin/env python3

from PIL import Image
import os, sys

ext = ".jpeg"
size = 128, 128
rotation = 90
dir = sys.argv[1]
new_dir = "./opt/icons/"

print(">>> dir: ", str(dir))

for infile in os.listdir(dir):
	if "ic_" not in infile:
		continue
	file, old_ext = os.path.splitext(infile)
	file_path = "/" + dir + "/" + infile
	print(">>> filepath: ", file_path)
	try:
		with Image.open(file_path) as im:
			im.rotate(rotation)
			im.resize(size)
			dest_path = new_dir + file + ext
			print(">>> dest : ", dest_path)
			im.save(dest_path, format="JPEG")
	except FileNotFoundError:
		print(f"File '{file_path}' not found.")