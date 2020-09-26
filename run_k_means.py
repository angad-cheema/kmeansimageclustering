# Angad Cheema cheem011
# Project 1, run_k_means module
# function for taking a file from the user and running k means
from k_means import *
'''
takes file name, k and output file name as input
applies k means function, then assigns each pixel to the average color of its respective cluster
saves the new image to the output file
'''

file = input("Input image file name: ")
k = int(input("Input number of colors: "))
output_file = input("Input output file name: ")

image = read_ppm(file)
means_list, assignments = k_means(image, k)    # does k means operation

width, height = get_width_height(image)
for x in range(width):
    for y in range(height):
        image[x][y] = means_list[assignments[x][y]]   # assigns each pixel to closest cluster mean

save_ppm(output_file, image)
print("Process completed, image saved to", output_file)
