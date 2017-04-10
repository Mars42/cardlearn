import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

h, w = 4, 4
img = Image.new("RGBA", (h,w),(20,10,40))
draw = ImageDraw.Draw(img)
fsize = h
font = ImageFont.truetype("/Library/Fonts/Chalkduster.ttf", fsize)
draw.text((0, h/2),"T",(255,45,100),font=font)
draw = ImageDraw.Draw(img)
img.save("a_test.png")