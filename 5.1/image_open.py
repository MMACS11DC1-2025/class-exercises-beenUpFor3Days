from PIL import Image

def isGreen(r,g,b):
    if r<25 and r>=0 and g>230 and g <=255 and b<25 and b>=0:
        return True
    return False

print(isGreen(0,255,0))

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()
