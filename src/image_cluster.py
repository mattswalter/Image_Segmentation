""" CISC684 Group 2 Homework 3"""
# =============================================================================
# #
# #  Created on Thu Nov  7 09:19:13 2019
# #
# #  CISC684: Group 2
# #
# #  @author: Matthew Walter <mswalter@udel.edu>
# #           Eric Allen <allenea@udel.edu>
# #           Murugesan Somasundaram <smuruges@udel.edu>
# #
# #  Command Line Execution:
# #  main.py <K> <input_image> <output_image> <show_image>
# =============================================================================
#IMPORTS
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.XYZ_Random_Centroids import XYZ_Random_Centroids
from src.dist import dist
# =============================================================================
# image = "ise.jpg"
# root_dir = os.getcwd()
# image_path = os.path.join(root_dir, "original_photos", image)
# # Choose K value for Random Clusters
# k = 2
# # Choose Image
# fname = "new_"+image.split(".")[0]+"_"+str(k)+".png"
# output_file = os.path.join(root_dir, "produced_photos", fname)
#
# show_image = True
# =============================================================================

def execute(k, image_path, output_file, show_image):
    """ Main Function """
    image = image_path.split("/")[-1]

    # Import Image
    image_raw = Image.open(image_path, 'r')
    image_data = np.array(image_raw.getdata())

    histo_rgb, _ = np.histogramdd(image_data, bins=256)
    r, g, b = np.nonzero(histo_rgb)

    r = r.flatten()
    g = g.flatten()
    b = b.flatten()

    if show_image:
        #plotting
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(r, g, b, color='blue', marker='.')
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')
        plt.title("Image: "+image.split(".")[0]+'\nRGB Colors')
        plt.show()

    # Randomly pick Center Cluster Points (RGB) in 3D Space (9 x 9)
    C_x, C_y, C_z = XYZ_Random_Centroids(image_data, k)
    C = np.array(list(zip(C_x, C_y, C_z)), dtype=np.int32)
    #print("Random Centroids:\n", C)


    if show_image:
        # Plot random cluster points
        fig = plt.figure()
        ax2 = Axes3D(fig)
        ax2.scatter3D(C_x, C_y, C_z, s=25.0, color='red', marker='X')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_zlabel('Z')
        plt.title('RGB Cluster Points')
        plt.show()

    # To store the value of centroids when it updates
    C_old = np.zeros(C.shape)
    # Cluster Lables(0, 1, 2)
    clusters = np.zeros(len(image_data))

    # Error func. - Distance between new centroids and old centroids
    error = dist(C, C_old, None)
    print("Starting Error: ", error)


    # Loop will run till the error becomes zero
    while error != 0:
        if np.isnan(error):
            print("Error. Try again.")
            sys.exit(0)

        # Assigning each value to its closest cluster
        for i in range(len(image_data)):
            distances = dist(image_data[i], C)
            cluster = np.argmin(distances)
            clusters[i] = cluster

        # Storing the old centroid values
        C_old = deepcopy(C)

        # Finding the new centroids by taking the average value for each cluster
        for i in range(k):
            points = [image_data[j] for j in range(len(image_data)) if clusters[j] == i]
            C[i] = np.mean(points, axis=0)

        error = dist(C, C_old, None)
        print("Minimizing Error: ", error)

    # C is RGB values of each cluster
    # Clusters is the cluster that each pixel value falls into.
    # Create an array by matching Cluster values to RGB Values
    new_cluster = []
    for i, classify in enumerate(clusters):
        for j, value in enumerate(C):
            if classify == j:
                new_cluster.append(list(C[j]))

    # =============================================================================
    # # Create and save clustered image
    # =============================================================================
    new_image = Image.fromarray(np.reshape(new_cluster,\
                        (image_raw.height, image_raw.width, 3)).astype(dtype=np.uint8))

    new_image.save(output_file, format="jpeg")

    if show_image:
        new_image.show()
