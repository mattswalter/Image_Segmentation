# K-Means Clustering

 By: Matthew Walter, Eric Allen, Murugesan Somasundaram

Libraries: numpy, os, sys, Image, random

Requires 4 arguments


#### K: integer (number of clusters)
#### input_image: valid file with path (.jpg/png)
#### output_image: valid file with path (.jpg/.png)
#### show_image:{yes,no}


## To Run
 > python main.py <K> <input_image> <output_image> <show_image>
 
## Example Run


For 2 clusters
 > python main.py 2 ./original_photos/ise.jpg ./produced_photos/new_ise_2.jpg no
 
For 3 clusters
 > python main.py 3 ./original_photos/ise.jpg ./produced_photos/new_ise_3.jpg no
 
For 5 clusters
 > python main.py 5 ./original_photos/ise.jpg ./produced_photos/new_ise_5.jpg no
 
For 10 clusters
 > python main.py 10 ./original_photos/ise.jpg ./produced_photos/new_ise_10.jpg no
 
For 20 clusters
 > python main.py 20 ./original_photos/ise.jpg ./produced_photos/new_ise_20.jpg no


