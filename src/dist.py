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
def dist(new_cent, old_cent, ax=1):
    """Euclidean Distance Caculator
    """#    ||A||_F = [\sum_{i,j} abs(a_{i,j})^2]^{1/2}
    return np.linalg.norm(new_cent - old_cent, axis=ax)

