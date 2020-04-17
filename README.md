# CISC684_Image_Segmentation
 Homework 3
 By: Eric Allen, Matthew Walter, Murugesan Somasundaram

Requires: Python3.7

Libraries: numpy, os, sys, Image, random

Requires 4 arguments and all image files should be provided in the directory with main.py


#### K: integer (Number of colors)
#### input_image: valid file with path (.jpg/png)
#### output_image: valid file with path (.jpg/.png)
#### show_image:{yes,no}


## To Run
 > python main.py <K> <input_image> <output_image> <show_image>
 
## Example Run

#### PHOTO 1

 > python main.py 2 ./original_photos/ise.jpg ./produced_photos/new_ise_2.jpg no
 
 > python main.py 3 ./original_photos/ise.jpg ./produced_photos/new_ise_3.jpg no
 
 > python main.py 5 ./original_photos/ise.jpg ./produced_photos/new_ise_5.jpg no
 
 > python main.py 10 ./original_photos/ise.jpg ./produced_photos/new_ise_10.jpg no
 
 > python main.py 20 ./original_photos/ise.jpg ./produced_photos/new_ise_20.jpg no


#### PHOTO 2

 > python main.py 2 ./original_photos/memorial.jpg ./produced_photos/new_memorial_2.jpg no
 
 > python main.py 3 ./original_photos/memorial.jpg ./produced_photos/new_memorial_3.jpg no
 
 > python main.py 5 ./original_photos/memorial.jpg ./produced_photos/new_memorial_5.jpg no
 
 > python main.py 10 ./original_photos/memorial.jpg ./produced_photos/new_memorial_10.jpg no
 
 > python main.py 20 ./original_photos/memorial.jpg ./produced_photos/new_memorial_20.jpg no
 

#### PHOTO 3

 > python main.py 2 ./original_photos/pearson.jpg ./produced_photos/new_pearson_2.jpg no
 
 > python main.py 3 ./original_photos/pearson.jpg ./produced_photos/new_pearson_3.jpg no
 
 > python main.py 5 ./original_photos/pearson.jpg ./produced_photos/new_pearson_5.jpg no
 
 > python main.py 10 ./original_photos/pearson.jpg ./produced_photos/new_pearson_10.jpg no
 
 > python main.py 20 ./original_photos/pearson.jpg ./produced_photos/new_pearson_20.jpg no
 

#### PHOTO 4 K = 2 BEST

 > python main.py 2 ./original_photos/box.jpg ./produced_photos/new_box_2.jpg no
 
 > python main.py 3 ./original_photos/box.jpg ./produced_photos/new_box_3.jpg no
 
 > python main.py 5 ./original_photos/box.jpg ./produced_photos/new_box_5.jpg no
 
 > python main.py 10 ./original_photos/box.jpg ./produced_photos/new_box_10.jpg no
 
 > python main.py 20 ./original_photos/box.jpg ./produced_photos/new_box_20.jpg no
