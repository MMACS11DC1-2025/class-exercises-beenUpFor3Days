from PIL import Image

'''''
def is_green(r,g,b):
    if r <100 and r >= 0 and g > 250 and g <= 255 and b < 100 and b >= 0:
        return True
    return False

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        im_r = image_green[i, j][0]
        im_g = image_green[i, j][1]
        im_b = image_green[i, j][2]

        if is_green(im_r, im_g, im_b):
            beach = image_beach[i, j]
            xy = (i,j)
            image_output.putpixel(xy, beach)

image_output.save("output.png", "png")
'''''

image_waterfall = Image.open("5.1/waterfall.jpg").load()

image_output = Image.open("5.1/waterfall.jpg")

width = image_output.width
height = image_output.height
r = image_waterfall[0, 0][0]
g = image_waterfall[0, 0][1]
b = image_waterfall[0, 0][2]

def is_light(pixel):
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            avg = int(r + g + b) / 3
            return avg >= 128

for x in range(width):
    for y in range(height):
        if is_light(image_waterfall[x, y]):
            image_output.putpixel((x, y), (255, 255, 255))
        else:
            image_output.putpixel((x, y), (0, 0, 0))

image_output.save("waterfallinvert.png", "png")



