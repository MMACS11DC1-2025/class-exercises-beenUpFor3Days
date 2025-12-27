Theme
This project analyzes outdoor photos with sky and evaluates how clear and blue the sky is in each image.

Visual Feature
The primary focus is on detecting clear blue sky pixels. The program sees every pixel, counts those that fit the blue sky criteria, and then calculates what percentage of the image consists of sky. That percentage becomes the sky clarity score.

Justification
Blue sky shows strong blue values, weaker red and green, and isn’t pure white. In my code, a pixel is labeled as sky if blue is high and clearly exceeds both red and green, and neither red nor green is strong enough to make the color white (like a cloud). This method identifies sky pixels while avoiding most clouds, glare, trees, buildings, or shadows.

Visual Feature and How It’s Detected
I created a function called is_target_feature. It checks each (r, g, b) pixel and returns True if the pixel matches the sky criteria. For each image, I loop over all the pixels, count the sky ones, and compute sky_percent as (sky_pixels * 100) // total_pixels. The final result is a straightforward statistical score—the fraction of pixels that appear as clear sky.

Algorithm Summary
I start by keeping at least ten image filenames in a list. For each image, I open it, scan every pixel using nested loops, count the sky pixels, calculate sky_percent, and store both the filename and score in image_scores. I use the time module to measure the process down to three decimal places. After all images are processed, I sort the results from highest to lowest using my own Selection Sort. I print the top five images by sky clarity with list slicing. After that, I prompt the user for a target sky percent and use my Binary Search to find that score in the sorted list.

Testing and Validation
I ran the program on at least ten images and confirmed it finished without errors. The scores make sense: images with more clear sky get higher percentages. Sorting functions correctly—highest scores appear first. Binary Search was tested with a score present in the list and one that was not, and the outcomes were accurate. I also tried entering letters at the search prompt—the program did not crash and instead displayed an error message.

Performance Analysis
The program reports the total processing time in seconds. Pixel scanning is the slowest part, since it examines every pixel in each image. Sorting and searching are quick, as there are only about ten results. Selection Sort is O(n²) and Binary Search is O(log n), but for this project size, both are sufficiently fast.

Challenges Faced
The hardest part was choosing sky thresholds that worked across different lighting and cloud conditions. I needed to adjust the values and test until the results matched what saw. Another challenge was making Binary Search function on a list sorted from highest to lowest, not the usual order. I also switched to using integer percentages for sky clarity so searching would not be affected by floating point rounding.

Real World Context
This project is a simplified version of what weather and satellite systems do when measuring cloud cover or clear sky. 

Files in This Project
readMe, explorer.py, PROJECT.md, and sky(1-10)