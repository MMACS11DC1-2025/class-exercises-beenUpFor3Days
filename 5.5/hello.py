import time
from PIL import Image
t0 = time.time()
file = Image.open("5.5/lowtaper.gif")
jbimg = file.load()

width = file.width
height = file.height

black = 0

for i in range(width):
    for j in range(height):
        r = jbimg[i, j][0]
        g = jbimg[i, j][1]
        b = jbimg[i, j][2]

        if r > 150 and g > 150 and b < 100:
            yellow_pixels += 1

print(yellow_pixels)
print(width * height)

percent_yellow = 100 * yellow_pixels / (width * height)
report = "There are {:.2f} percent yellow jellybeans.".format(percent_yellow)
t1 = time.time()
entire = t1 - t0
timings = "it took {:.2f}s to lead the whole code".format(entire)
print(timings)
print(report)