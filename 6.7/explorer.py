from PIL import Image
import time

folder = "6.7"

image_files = [
    "Sky1.jpg",
    "sky2.jpg",
    "sky3.jpg",
]

def is_target_feature(pixel):
    r, g, b = pixel
    if b >= 120 and b >= r + 20 and b >= g + 20 and r <= 220 and g <= 220:
        return True
    else:
        return False

def selection_sort(data):
    n = len(data)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if data[j][1] > data[max_index][1]:
                max_index = j
        temp = data[i]
        data[i] = data[max_index]
        data[max_index] = temp

def binary_search(data, target):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        value = data[mid][1]
        if value == target:
            return mid
        elif value < target:
            last = mid - 1
        else:
            first = mid + 1
    return -1

image_scores = []

start_time = time.time()

for filename in image_files:
    print("Processing:", filename)
    img = Image.open(folder + "/" + filename)
    pixels = img.load()
    width, height = img.size
    total_pixels = width * height
    sky_pixels = 0

    for x in range(width):
        for y in range(height):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if is_target_feature((r, g, b)):
                sky_pixels += 1

    sky_percent = (sky_pixels * 100) // total_pixels
    image_scores.append([filename, sky_percent])

end_time = time.time()
elapsed = end_time - start_time
print("\nProcessing time: {:.3f} seconds".format(elapsed))

selection_sort(image_scores)

top5 = image_scores[:5]
print("\nTop images (clearest sky first):")
for item in top5:
    name = item[0]
    percent = item[1]
    print("{} : {}% sky".format(name, percent))

answer = input("\nEnter sky % to search for (exact integer shown, or press Enter to skip): ")
if answer != "":
    target = int(answer)
    index = binary_search(image_scores, target)
    if index != -1:
        result = image_scores[index]
        print("Found: {} with {}% sky".format(result[0], result[1]))
    else:
        print("No match")
