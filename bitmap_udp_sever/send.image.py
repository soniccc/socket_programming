from PIL import Image

image = Image.open("nat.bmp")

width, height = image.size
print(width, height)

for y in range(height):
    for x in range(width):
        pos = (x, y)
        rgba = image.getpixel(pos)
        print(pos, rgba)


