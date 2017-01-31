from PIL import Image, ImageDraw

Image.open("images/frog.jpg").save("images/1.png")
image = Image.open("images/1.png")
img = image.convert("RGBA")
width = img.size[0]
height = img.size[1]
pix = img.load()

for i in range(width):
    for j in range(height):
       
        if pix[i, j][0] == 255 and pix[i, j][1] == 255 and pix[i, j][2] == 255 and pix[i, j][3] == 255:
            pix[i, j] = (0, 0, 0, 0)

img.save("images/new/new.png", "PNG")

