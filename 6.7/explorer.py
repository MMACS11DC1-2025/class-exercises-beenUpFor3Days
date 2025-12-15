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
    # Simple thresholds for clear blue sky:
    # - blue is fairly bright
    # - blue is clearly higher than red and green
    if (
        b >= 120 and
        b >= r + 20 and
        b >= g + 20 and
        r <= 220 and g <= 220
    ):
        return True
    else:
        return False

# main program
image_scores = []

# start timing
start = time.time()

# loop through images
for img in image_files:
    print("Processing:", img)

    # open the image
    image = Image.open(f"{folder}/{img}")
    image = image.convert("RGB")
    width, height = image.size
    total_pixels = width * height
    sky_pixel_count = 0

    # count the sky pixels
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            if is_sky((r, g, b)):
                sky_pixel_count += 1

    sky_percent = sky_pixel_count / total_pixels * 100
    image_scores.append([img, sky_percent])

# end timing
end = time.time()
print(f"\nProcessing time: {end - start:.3f} seconds")

# selection sort by sky % (descending)
for i in range(len(image_scores)):
    largest_score = image_scores[i][1]
    largest_index = i
    for j in range(i + 1, len(image_scores)):
        if image_scores[j][1] > largest_score:
            largest_score = image_scores[j][1]
            largest_index = j
    image_scores[largest_index], image_scores[i] = image_scores[i], image_scores[largest_index]

# print top 5 images
print("\nTop images (clearest sky first):")
for i in range(min(5, len(image_scores))):
    print(image_scores[i][0], "-", round(image_scores[i][1], 2), "% sky")

# binary search for user-input sky %
query = input("\nEnter sky % to find (or skip): ")
if query != "":
    target = float(query)
    found = False
    first = 0
    last = len(image_scores) - 1
    tol = 0.01

    while first <= last:
        mid = (first + last) // 2
        mid_value = image_scores[mid][1]

        if abs(mid_value - target) <= tol:
            print("Found:", image_scores[mid][0], "-", round(mid_value, 2), "% sky")
            found = True
            break
        # list is sorted high → low
        elif mid_value < target:
            last = mid - 1
        else:
            first = mid + 1

    if not found:
        print("No match")
