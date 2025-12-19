PROJECT OVERVIEW

Theme
This project analyzes a set of outdoor photos that contain sky. The goal is to measure how clear and blue the sky is in each image.

Visual Feature
The visual feature detected is clear blue sky pixels. For each image, the program decides which pixels are sky pixels and then calculates what percent of the image is sky. This percent is the sky clarity score for that image.

Justification
Clear blue sky usually has a strong blue color and weaker red and green. It is also not extremely dark and not pure white. In my code, a pixel is counted as sky if:

The blue value is high enough.

The blue value is clearly higher than the red and green values.

The red and green values are not so high that the pixel becomes almost white.

This rule helps focus on blue sky regions and avoid clouds, glare, trees, buildings and shadows as much as possible.

VISUAL FEATURE AND HOW IT IS DETECTED

I use a function called is_target_feature that takes one pixel as input. The pixel is an r, g, b tuple.

Inside the function, I compare the red, green and blue values. The function returns True if the pixel is likely clear blue sky and False otherwise.

The rule (with the thresholds I use in my code) is:

Blue is bright enough.

Blue is at least a bit higher than red.

Blue is at least a bit higher than green.

Red and green are not extremely high.

For each image, I loop over every pixel, call is_target_feature on that pixel, and count how many pixels return True. I then compute an integer sky percentage using:

sky_percent = (sky_pixels * 100) // total_pixels

This sky_percent value is the feature density score for the image. A higher score means more of the image is clear blue sky.

ALGORITHM SUMMARY

High level steps of the program:

Make a list of image filenames.

For each image in the list:
a) Open the image from the folder.
b) Look at every pixel using nested for loops over x and y.
c) Use the is_target_feature function to decide if the pixel is a sky pixel.
d) Count how many pixels are sky pixels.
e) Compute the sky percentage for that image.
f) Store [filename, sky_percent] in a list called image_scores.

Measure how long all of the image processing takes using the time module.

Use Selection Sort to sort image_scores from highest sky percentage to lowest sky percentage.

Use list slicing to take the first five items and print the top 5 images with the clearest sky.

Ask the user to enter a sky percentage.

Use Binary Search on the sorted image_scores list to look for an image with that sky percentage.

If a match is found, print the image name and its sky percentage. If not, print that there is no match.

TESTING AND VALIDATION

I tested the program in the following ways:

Basic run test
I ran the program on at least ten sky images. The program opened every image, processed all pixels and finished without crashing.

Visual check of percentages
I compared the printed sky percentages with what the images looked like by eye. Images that had a lot of clear blue sky had higher percentages. Images with more clouds, trees, buildings or ground had lower percentages. This showed that the feature rule for sky pixels works reasonably well.

Testing the sorted order
After Selection Sort, I checked that the sky percentages in image_scores go from highest to lowest. The top five printed images matched the images that looked the most clear by eye.

Testing Binary Search
I looked at the printed sky percentages and picked one of the integer values, for example 62. I entered 62 at the search prompt and the program found the correct image and printed its name. I also entered a value that no image had, and the program correctly printed that there was no match.

PERFORMANCE ANALYSIS

The program measures how long the full image processing takes using the time module. It prints a line such as:

Processing time: X.XXX seconds

Most of the time is spent in the nested loops that visit every pixel of every image. For each image, the program does width times height checks, so the cost grows with the number of pixels in each image and with the number of images.

The other parts of the program are much faster:

Selection Sort
Selection Sort has time complexity proportional to n squared, where n is the number of images. In this project n is about ten, so it still runs quickly and is easy to understand.

Binary Search
Binary Search has time complexity proportional to log n, which is very small for a list of about ten items.

For this small project, the simple pixel loops plus Selection Sort and Binary Search are efficient enough.

CHALLENGES FACED

Choosing sky thresholds
One challenge was picking good comparison values for red, green and blue. If the rule was too strict, the program missed real sky pixels, especially in darker or hazy images. If the rule was too loose, the program sometimes counted blue objects like roofs, water or signs as sky. I adjusted the values so that blue only needs to be a bit higher than red and green, and I ignored pixels that were very dark or very close to white. This made the sky percentages better match what I saw in the images.

Binary Search on a descending list
Another challenge was getting Binary Search to work correctly when the list is sorted from highest percentage to lowest percentage instead of lowest to highest. I had to think carefully about when to move the search range left or right based on whether the middle value was less than or greater than the target value. After adjusting the conditions, the search started returning the correct index.

Integer percentages instead of decimals
At first I used decimal percentages. When I tried to search using exact equality, the values did not always match because of rounding differences. I changed the code so that the sky percentage is an integer from 0 to 100. This made it easy to search for exact integer percentages and made Binary Search simpler and more reliable.

REAL WORLD CONTEXT

This project is a small example of how computer vision and image analysis can work in real life. Weather and satellite systems often estimate things like cloud cover and clear sky fraction. They classify pixels in an image into different classes, such as cloud, clear sky, land and water, and then compute percentages for each class.

My project uses a simple rule to detect clear blue sky pixels and then calculates the percentage of sky pixels in a normal photo. It is a simplified version of the same idea: classify pixels into a category and then measure how much of the image belongs to that category.

FILES IN THIS PROJECT

Python code file
Contains:

The is_target_feature function to detect sky pixels.

The selection_sort function to sort images by sky percentage.

The binary_search function to search for a specific sky percentage.

The main code that:
a) Processes every image in the image_files list,
b) Computes sky percentages,
c) Times the processing,
d) Sorts the list of results,
e) Prints the top five images,
f) Asks the user for a target percentage and searches for it.

README file
Explains the project theme, the visual feature, the algorithm, the testing and validation, the performance analysis, the challenges faced and the real world context.

Image files
At least ten sky related images stored in the folder used by the program. Each image is used as input to calculate a sky clarity score.