from PIL import Image
import time

folder = "6.7"

image_files = [
    "Sky1.jpg",
    "sky2.jpg",
    "sky3.jpg",
]

def is_sky(pixel):
    r, g, b = pixel
    return b >= 120 and b >= r + 20 and b >= g + 20 and r <= 220 and g <= 220

def selection_sort(scores):
    n = len(scores)
    for i in range(n):
        largest_index = i
        for j in range(i + 1, n):
            if scores[j][1] > scores[largest_index][1]:
                largest_index = j
        scores[i], scores[largest_index] = scores[largest_index], scores[i]

def binary_search(scores, target, tol):
    first = 0
    last = len(scores) - 1
    while first <= last:
        mid = (first + last) // 2
        value = scores[mid][1]
        if abs(value - target) <= tol:
            return mid
        elif value < target:
            last = mid - 1
        else:
            first = mid + 1
    return -1

image_scores = []

start = time.time()

for img in image_files:
    print("Processing:", img)
    image = Image.open(f"{folder}/{img}")
    image = image.convert("RGB")
    width, height = image.size
    total_pixels = width * height
    sky_pixels = 0
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if is_sky((r, g, b)):
                sky_pixels += 1
    sky_percent = sky_pixels / total_pixels * 100
    image_scores.append([img, sky_percent])

end = time.time()
print(f"\nProcessing time: {end - start:.3f} seconds")

selection_sort(image_scores)

top5 = image_scores[:5]
print("\nTop images (clearest sky first):")
for name, percent in top5:
    print(name, ":", round(percent, 2), "% is sky")

query = input("\nEnter sky % to find (or press Enter to skip): ")
if query != "":
    target = float(query)
    index = binary_search(image_scores, target, 0.01)
    if index != -1:
        name, percent = image_scores[index]
        print("Found:", name, "-", round(percent, 2), "% sky")
    else:
        print("No match")
