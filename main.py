#!/usr/bin/python

import os, sys
import shutil
import csv
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

h, w = 400, 600
font_size = 40
folder = "cards"

def MakeImage(text, fname, side):
	img = Image.new("RGBA", (w,h), (84,81,178))
	draw = ImageDraw.Draw(img)
	if side == 1:
		font = ImageFont.truetype("MIROSLN.ttf", font_size)
	else:
		font = ImageFont.truetype("/Library/Fonts/Chalkboard.ttc", font_size)
	draw.text(((w - (len(text)*font_size*0.4))/2, h*0.4), text, (98,253,145), font=font)
	draw = ImageDraw.Draw(img)
	img.save(fname)

def ClearContent(folder_):
	for the_file in os.listdir(folder_):
		file_path = os.path.join(folder_, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print(e)

def main():
	assert len(sys.argv) != 1, "Usage: python main.py <file_name>"

	if len(sys.argv)-1 == 1:
		ClearContent(folder)

	count = 1
	with open(sys.argv[1], newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
			fname_a = folder + ("/%02d_a.jpg" % count)
			fname_b = folder + ("/%02d_b.jpg" % count)
			MakeImage(row[0].strip(), fname_a, 0)
			MakeImage(row[1].strip(), fname_b, 1)
			count += 1

if __name__ == '__main__':
	main()