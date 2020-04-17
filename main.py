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
# #  python main.py <K> <input_image> <output_image> <show_image>
# #
# # PHOTO 1
# #  python main.py 2 ./original_photos/ise.jpg ./produced_photos/new_ise_2.jpg no
# #  python main.py 3 ./original_photos/ise.jpg ./produced_photos/new_ise_3.jpg no
# #  python main.py 5 ./original_photos/ise.jpg ./produced_photos/new_ise_5.jpg no
# #  python main.py 10 ./original_photos/ise.jpg ./produced_photos/new_ise_10.jpg no
# #  python main.py 20 ./original_photos/ise.jpg ./produced_photos/new_ise_20.jpg no
# #
# # PHOTO 2
# #  python main.py 2 ./original_photos/memorial.jpg ./produced_photos/new_memorial_2.jpg no
# #  python main.py 3 ./original_photos/memorial.jpg ./produced_photos/new_memorial_3.jpg no
# #  python main.py 5 ./original_photos/memorial.jpg ./produced_photos/new_memorial_5.jpg no
# #  python main.py 10 ./original_photos/memorial.jpg ./produced_photos/new_memorial_10.jpg no
# #  python main.py 20 ./original_photos/memorial.jpg ./produced_photos/new_memorial_20.jpg no
# #
# # PHOTO 3
# #  python main.py 2 ./original_photos/pearson.jpg ./produced_photos/new_pearson_2.jpg no
# #  python main.py 3 ./original_photos/pearson.jpg ./produced_photos/new_pearson_3.jpg no
# #  python main.py 5 ./original_photos/pearson.jpg ./produced_photos/new_pearson_5.jpg no
# #  python main.py 10 ./original_photos/pearson.jpg ./produced_photos/new_pearson_10.jpg no
# #  python main.py 20 ./original_photos/pearson.jpg ./produced_photos/new_pearson_20.jpg no
# #
# # PHOTO 4 K = 2 BEST
# #  python main.py 2 ./original_photos/box.jpg ./produced_photos/new_box_2.jpg no
# #  python main.py 3 ./original_photos/box.jpg ./produced_photos/new_box_3.jpg no
# #  python main.py 5 ./original_photos/box.jpg ./produced_photos/new_box_5.jpg no
# #  python main.py 10 ./original_photos/box.jpg ./produced_photos/new_box_10.jpg no
# #  python main.py 20 ./original_photos/box.jpg ./produced_photos/new_box_20.jpg no
# =============================================================================
#IMPORTS
from __future__ import print_function
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.image_cluster import execute

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

def main():
    if len(sys.argv) < 4:
        print("INVALID INPUT")
        print("python main.py <K> <input_image> <output_image> <show_image>")
        sys.exit(0)
    else:
        yes_no = False
        if str((sys.argv[4])).upper() == "YES":
            yes_no = True
        if sys.argv[1].isdigit() and not isinstance(int(sys.argv[1]), int):
            print("<K> value was found to not be an integer type. Must be INT type.")
            print("python main.py <K> <input_image> <output_image> <show_image>")
            sys.exit(0)
        else:
            K = int(sys.argv[1])
    execute(K, sys.argv[2], sys.argv[3], yes_no )

if __name__ == "__main__":  
    main()