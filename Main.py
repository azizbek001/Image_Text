import os
from PIL import Image, ImageDraw, ImageFont
from random import randint
img = Image.open('iT .jpg')

draw = ImageDraw.Draw(img)

name = ImageFont.truetype('Gabriola.ttf', size=355)

text = input("Sevgan Qizingizning Ismi >> ")

draw.text((((600 - len(text) * 20) / 2), 280), text, font=name)

img.save('I Love You.bmp')

img.show()