from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("a_test.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("/Library/Fonts/Chalkduster.ttf", 16)
draw.text((0, 0),"Sample Text",(255,255,255),font=font)
img.save('sample-out.jpg')