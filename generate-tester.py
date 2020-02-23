from PIL import Image

width = 212
height = 104

img = Image.new( 'L', (width, height), "white")
pixels = img.load()
for x in range(width):
    for y in range(height):
        pixels[x,y] = (255 - int(x/width*255))

img.save('pic/tester-black.bmp','BMP')

img = Image.new( 'L', (width, height), "white")
pixels = img.load()
for x in range(width):
    for y in range(height):
        pixels[x,y] = (int(x/width*255))

img.save('pic/tester-red.bmp','BMP')

