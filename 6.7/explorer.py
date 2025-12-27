# Algorithm:
# 1. Make a list of image filenames.
# 2. For each image in the list:
#    Open the image.
#    Look at every pixel.
#    Count how many pixels are "sky pixels" using is_target_feature.
#    Compute the percentage of sky pixels and add [filename, percent] to image_scores.
# 3. Measure and print how long this processing takes.
# 4. Sort image_scores from highest percentage to lowest using selection_sort.
# 5. Print the top 5 images with the highest sky percentages.
# 6. Ask the user for a sky percentage.
# 7. Use binary_search on the sorted list to find an image with that percentage.


from PIL import Image
import time

folder = "6.7"
#all the pictures
image_files = (
    "Sky1.jpg",
    "sky2.jpg",
    "sky3.jpg",
    "sky4.jpg",
    "sky5.jpg",
    "sky6.webp",
    "sky7.jpg",
    "sky8.webp",
    "sky9.jpg",
    "sky10.webp"
)
#function to see if the pixle is white or blue
def is_target_feature(pixel):
    r, g, b = pixel
    brightness = (r + g + b) // 3
    if brightness > 210:          
        return False
    if b >= 90 and b >= r + 10 and b >= g + 10 and r <= 230 and g <= 230:
        return True
    else:
        return False

#selection sort
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
#binary search
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

#defins image_scores as a list
image_scores = []

#starts prosessing timer
start_time = time.time()

#for loop to get all the images
for filename in image_files:
    print("Processing:", filename)
    img = Image.open(folder + "/" + filename)
    pixels = img.load()
    width, height = img.size
    total_pixels = width * height
    sky_pixels = 0
#goes through each pixle 
    for x in range(width):
        for y in range(height):
            r = pixels[x, y][0]
            g = pixels[x, y][1]
            b = pixels[x, y][2]
            if is_target_feature((r, g, b)):
                sky_pixels += 1
#takes blue pixles and divides with total pixles
    sky_percent = (sky_pixels * 100) // total_pixels
    image_scores.append([filename, sky_percent])
#end timeer
end_time = time.time()
elapsed = end_time - start_time
print("\nProcessing time: {:.3f} seconds".format(elapsed))

selection_sort(image_scores)
#prints top 5 images with percentage 
top5 = image_scores[:5]
print("\nTop images (clearest sky first):")
for item in top5:
    name = item[0]
    percent = item[1]
    print("{} : {}% sky".format(name, percent))


#find the picture based off the users input of sky %
answer = input("\nEnter sky % to search for: ")
if answer != "":
    target = int(answer)
    index = binary_search(image_scores, target)
    if index != -1:
        result = image_scores[index]
        print("Found: {} with {}% sky".format(result[0], result[1]))
    else:
        print("No match")