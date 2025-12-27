from PIL import Image

def is_yellow(r,g,b):
    if r < 40 and g > 90 and b < 10:
        return True
    return False

def is_

image = Image.open("5.4/jelly_beans.jpg").load()
image_output = Image.open("5.4/jelly_beans.jpg")
width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        im_r = image[i, j][0]
        im_g = image[i, j][1]
        im_b = image[i, j][2]

        if is_yellow(im_r, im_g, im_b):
            image_output.putpixel((i, j), (255, 255, 255))

image_output.save("newBeans.png", "png")
