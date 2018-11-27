#import the following python libraries:
import gzip
#import PIL.Image as pil
from PIL import Image  # image library
import numpy as np


# Parse all images in the given file to a list.
def parse_images(images_path):
		# Open the image gzip in read bytes mode.

    with gzip.open(images_path, 'rb') as file:
		# Read the first four bytes i.e. the magic number.
	    magic = file.read(4)
        #magic = int.from_bytes(magic, 'big')
        print("Magic number: " +, magic)

		# Read the next four bytes i.e. the number of images.
	    number_of_images = int.from_bytes(file.read(4), 'big')
        print("Number of images: ", number_of_images)

		# Read the next four bytes i.e. the number of rows.
	    rows = int.from_bytes(file.read(4), 'big')
        print("Number of rows: ", rows)

		# Read the next four bytes i.e. the number of cols.
	    columns = int.from_bytes(file.read(4), 'big')
        print("Number of cols: ", columns)
    

print() # break
        
			
			
	
