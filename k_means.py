# Angad Cheema cheem011
# Project 1, k_means module
# contains functions for k means clustering
import math
from image_utils import *

'''
# returns a list of k random colors, using the random colors function given
def initial_guess(k):
    means_list = []
    for i in range(k):
        means_list.append(random_color())
    return means_list
'''

'''
returns a list of k random colors, picks random colors from the image instead of random colors
I used this function instead because it provided better convergence
'''
def initial_guess(k, image):
    means_list = []
    width, height = get_width_height(image)
    for i in range(k):
        means_list.append(image[random.randrange(width)][random.randrange(height)])
    return means_list


'''
computes and returns euclidean distance between two vectors
'''
def vector_distance(vector1, vector2):
    distance_sum = 0
    for i in range(len(vector1)):
        distance_sum += ((vector1[i] - vector2[i]) ** 2)
    return math.sqrt(distance_sum)


'''
Given a vector and list of means, the function returns the index of the mean in the list that is closest to the vector
'''
def min_distance(vector, means_list):
    minimum_distance = vector_distance(vector, means_list[0])
    min_index = 0
    for i in range(1, len(means_list)):
        dist = vector_distance(vector, means_list[i])
        if dist < minimum_distance:
            minimum_distance = dist
            min_index = i
    return min_index


'''
This function takes the image array, assignments array, and means list and traverses through assignments list and updates the assignments
the function updates the assignments array that is an input instead of creating and returning a new assignments array
'''
def update_assignments(image, assignments, means_list):
    width, height = get_width_height(image)
    for x in range(width):
        for y in range(height):
            assignments[x][y] = min_distance(image[x][y], means_list)  # assigns pixel to mean with smallest distance


'''
Takes the image array, assignments array, and means list and traverses through image and calculates new means
Updates the means list instead of creating and returning a new means list
Has a list sum_list that stores k 4-lists containing the sum of r, g, b, components, and number of pixels assigned to that color
The list at sum_list[i] corresponds to the color of means_list[i]
traverses through the image once, checks assignments to know which list in sum_list to add to
Uses elements of each list in sum_list to calculate the average of each cluster for the new color for means_list
'''
def update_means(image, assignments, means_list):
    width, height = get_width_height(image)
    k = len(means_list)
    sum_list = []  # contains k lists, each list contains sum of r components, g components, b components, and number of pixels with that assignment
    for i in range(k):  # initializes sum_list
        row = [0, 0, 0, 0]
        sum_list.append(row)

    for x in range(width):
        for y in range(height):  # traverses through each pixel in the image
            color = assignments[x][y]  # checks mean assignment
            sum_list[color][3] += 1  # increase that mean's quantity count by 1
            for i in range(3):
                sum_list[color][i] += image[x][y][i]  # increases r,g,b sum for that mean

    for color in range(k):  # traverses means list, calculates average color from values in sum_list
        if sum_list[color][3] != 0:
            means_list[color] = (
                round(sum_list[color][0] / sum_list[color][3]), round(sum_list[color][1] / sum_list[color][3]),
                round(sum_list[color][2] / sum_list[color][3]))


'''
Final k means function, takes image array and k as inputs, returns tuple with means list and assignments array
iterates assignment and new mean calculation until means do not change 
'''
def k_means(image, k):
    width, height = get_width_height(image)
    means_list = initial_guess(k, image)  # creates initial guess of means
    assignments = []
    for columnNum in range(width):  # initializes assignments array as list of list of integers
        row = [0] * height
        assignments.append(row)

    prev_means_list = means_list  # this means list stores the original means list, used to check for convergence, when the means have not changed
    update_assignments(image, assignments, means_list)  # updates assignments
    update_means(image, assignments, means_list)
    while means_list != prev_means_list:  # iterates until means do not change
        prev_means_list = means_list
        update_assignments(image, assignments, means_list)
        update_means(image, assignments, means_list)
    return (means_list, assignments)  # returns tuple of means_list and assignments
