from PIL import Image, ImageDraw, ImageFont
import os

def generate_images(num):
  im = Image.new("RGB", (300, 300), "blue")
  draw = ImageDraw.Draw(im)
  fnt = ImageFont.truetype("~/Library/Fonts/Ricty-Regular.ttf", size=300)
  draw.text((0, 0), str(num), font=fnt)
  if not os.path.exists('./test-images'):
    os.mkdir('./test-images')
  im.save("./test-images/body" + str(num) + ".png")

def generate_revealment_images():
  im = Image.new("RGB", (300, 300), "blue")
  draw = ImageDraw.Draw(im)
  fnt = ImageFont.truetype("~/Library/Fonts/Ricty-Regular.ttf", size=300)
  draw.text((0, 0), 'XX', font=fnt)
  im.save("./xx.png")

print('How many images do you need?\nIf you need an image for revealment, type 0')
count = int(input('>> '))

if count == 0:
  generate_revealment_images()
else:
  for i in range(count):
    generate_images(i)
