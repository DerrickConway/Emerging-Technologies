import gzip
from PIL import Image
import numpy as np

def parse_images(images_path):
    with gzip.open(images_path, 'rb') as file:

        magic = int.from_bytes(file.read(4), 'big')
        print(" Magic number: " + str(magic))


        number_of_Images = int.from_bytes(file.read(4), 'big')
        print("Number of Images: " + str(number_of_Images))


        rows = int.from_bytes(file.read(4), 'big')
        print("Number of rows; " + str(rows))


        columns = int.from_bytes(file.read(4), 'big')
        print("Number of Columns: " + str(columns))



      

#print()

        


