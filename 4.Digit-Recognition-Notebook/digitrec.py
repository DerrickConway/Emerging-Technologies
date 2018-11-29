import gzip
from PIL import Image
import numpy as np

#self.name = name




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

      #  buffer = file.read(rows * columns * number_of_Images)
     #   data = np.frombuffer(buffer, dtype=np.uint8)
    #    self.images = data.reshape(number_of_Images, rows, columns)


def parse_labels(labels_path):
    with gzip.open(labels_path, 'rb') as file:

        magic = int.from_bytes(file.read(4), 'big')
        print("Magic number: " + str(magic))


        number_of_labels = int.from_bytes(file.read(4), 'big')
        print("Number of labels: " + str(number_of_labels))







      

#print()

        


