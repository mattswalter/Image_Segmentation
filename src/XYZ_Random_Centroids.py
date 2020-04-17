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
# #
# =============================================================================
#IMPORTS
import numpy as np
def XYZ_Random_Centroids(data, k):
    """Calculate Mean Cluster Values"""
    # X coordinates of random centroids
    C_x = np.random.randint(0, np.max(data)-20, size=k)

    # Y coordinates of random centroids
    C_y = np.random.randint(0, np.max(data)-20, size=k)

    # Z coordinates of random centroids
    C_z = np.random.randint(0, np.max(data)-20, size=k)
    return C_x, C_y, C_z