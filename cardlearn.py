#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

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

script_path = os.path.dirname(os.path.realpath(__file__))

def IsEng(text):
	return (ord(text[0]) >= ord('A') and ord(text[0]) <= ord('z'))

def MakeImage(text, fname):
	img = Image.new("RGBA", (w,h), (84,81,178))
	draw = ImageDraw.Draw(img)

	if IsEng(text):
		font = ImageFont.truetype("/Library/Fonts/Chalkboard.ttc", font_size)
	else:
		font = ImageFont.truetype(os.path.join(script_path, "MIROSLN.ttf"),\
		 															font_size)

	draw.text(((w - (len(text)*font_size*0.4))/2, h*0.4), text, (98,253,145),\
																	font=font)
	draw = ImageDraw.Draw(img)
	img.save(fname)

def ClearContent(folder_):
	if os.path.isdir(folder_):
		for the_file in os.listdir(folder_):
			file_path = os.path.join(folder_, the_file)
			try:
				if os.path.isfile(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print(e)
	else:
		print("No such folder: {}. Created".format(folder_))
		os.mkdir(folder_)

def main():
	assert len(sys.argv) != 1, "Usage: python cardlearn.py <file_name>"

	if len(sys.argv)-1 == 1:
		if not (sys.argv[1].endswith(".csv") or sys.argv[1].endswith(".txt")):
			assert 0, "Wrong format. Use .csv or .txt"
		print("Clearing...")
		ClearContent(folder)

	count = 1
	with open(sys.argv[1], newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		print("Fetching words...")
		for row in spamreader:
			fname_a = folder + ("/%02d_a.jpg" % count)
			fname_b = folder + ("/%02d_b.jpg" % count)
			MakeImage(row[0].strip(), fname_a)
			MakeImage(row[1].strip(), fname_b)
			count += 1
	print("Done!")

if __name__ == '__main__':
	main()
