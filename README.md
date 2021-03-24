# kmeansimageclustering
Clusters colors in an image using k means. Written in python 3.

Takes an image in ppm format, returns another ppm image with only a given number of colors.
Examples of input and output are shown.

image_utils.py contains the functions for opening and saving ppm images.

k_means.py contains functions for k means clustering.

run_k_means.py contains the main function for taking an input image and saving a new image.

Southeast_Steam_Plant-University_of_Minnesota.ppm is used under the Creative Commons Attribution 2.0 Generic License. See https://en.wikipedia.org/wiki/File:Southeast_Steam_Plant-University_of_Minnesota.jpg for more information. I chose this as I thought it would be a difficult image for the algorithm.

# How to use
1. Download/clone/etc the repository
2. Using Python 3, run the file `run_k_means.py`
3. The image path will be asked for as console input. The image must be in .ppm format.
4. The next console input will be for how many different colors the output should image have. This is the number of clusters.
5. The final input will be the path of the output file.

Modules needed: random

# Methods
Opens an image and creates an array of every pixel in the image. Clusters these pixels to a given number of pixels using the k means method. Returns the image, but with each pixel recolored to its respective cluster.

Given the image and n clusters to create as user input, it randomly assigns the colors of n random pixels to be the cluster centers. It then iterates through each pixel, calculates which cluster center it is closest to and assigns it to that cluster. Then it iterates through each cluster and recalculates the cluster center. It repeats this process until the cluster centers do not change. It then colors each pixel to be the color of its respective cluster and then returns the image.
