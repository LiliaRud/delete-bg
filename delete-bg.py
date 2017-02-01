from PIL import Image, ImageDraw
from os import listdir

imagesJpg = listdir("images")

for a in imagesJpg:
    if a[-3:] == "jpg":
        Image.open("images/" + a).save("images/png/" + a + ".png")

imagesPng = listdir("images/png")

for a in imagesPng:
    if a[-3:] == "png":
        image = Image.open("images/png/" + a)
        img = image.convert("RGBA")
        width = img.size[0]
        height = img.size[1]
        pix = img.load()

        for i in range(width):
            for j in range(height):
               
                if pix[i, j][0] == 255 and pix[i, j][1] == 255 and pix[i, j][2] == 255 and pix[i, j][3] == 255:
                    pix[i, j] = (0, 0, 0, 0)

        img.save("images/new/" + a, "PNG")

