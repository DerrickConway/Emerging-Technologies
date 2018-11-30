import gzip
from PIL import Image
import numpy as np


#download the image and lade files, have python decompress them byte by byte in order

#read gzip files

#self.name = name


#class MnistDataSet:
#def __init__(self, name, image_Path, lable_path):
   # self.name = name

    #self.parse_images(image_Path)
 #   self.parse_labels(lable_path)

#------------------------------------------------------------
# step one - read in the data file for this section im reading in images file


#def parse_images(self, images_path):
def parse_images(images_path):
            
    with gzip.open(images_path, 'rb') as file: #open file with gzip
        magic = int.from_bytes(file.read(4), 'big') # convert bites to int format, using magic number for the first 4 bytes, 'big' = most signficant byte first
        #magic = int.from_bytes(file.read(4), 'big') 
        print(" Magic number: " + str(magic)) # print magic number 

        #reads in nunber of images by first 4 bytes
        number_of_Images = int.from_bytes(file.read(4), 'big')
        print(" Number of Images: " + str(number_of_Images)) # prints number of images

        #reads in number of rows by first 4 bytes
        rows = int.from_bytes(file.read(4), 'big')
        print(" Number of rows; " + str(rows))#prints number of rows

        #reads in number of columns by first 4 bytes
        columns = int.from_bytes(file.read(4), 'big')
        print(" Number of Columns: " + str(columns))# prints number of columns

       # buffer = file.read(rows * columns * number_of_Images)
       # data = np.frombuffer(buffer, dtype=np.uint8)
      #  self.images = data.reshape(number_of_Images, rows, columns)

        images = [] # array created for images
        for i in range(number_of_Images): # for loop for number of images
            rowss = [] # ararry created for rows
            for r in range(rows): # loop for rows
                columnss = [] # array for columns
                for c in range(columns): # loop for columns
                    columnss.append(int.from_bytes(file.read(1), 'big')) # using append for every column to add byte to the column array
                rowss.append(columnss) # use append to add columns array to every row
            images.append(rowss) #use append to add rows array to every image / rows + columns = image
        return images # return the image

print()



# pass through filenames to read images funtion
trainImages = parse_images('train-images-idx3-ubyte.gz')
testImages = parse_images('t10k-images-idx3-ubyte.gz')


#---------------------------------------------------------------

# step two
# read in the data file for this section im reading in labels file

def parse_labels(labels_path): # reading in the labels file
    with gzip.open(labels_path, 'rb') as file: #open file with gzip

        magic = int.from_bytes(file.read(4), 'big') # convert bites to int format, using magic number for the first 4 bytes, 'big' = most signficant byte first
        print(" Magic number: " + str(magic)) # print magic number 

        # reads in nunber of labels by first 4 bytes
        number_of_labels = int.from_bytes(file.read(4), 'big')
        print(" Number of labels: " + str(number_of_labels)) # prints number of labels


        labels =[file.read(1) for i in range(number_of_labels)] # read file byte by byte and store in array
        labels = [int.from_bytes(label, 'big') for label in labels] # overwrite the labels array with ints instead of bytes

        return labels

print()

# pass through filenames to read labels funtion
translabels = parse_labels('train-labels-idx1-ubyte.gz')
testlabels = parse_labels('t10k-labels-idx1-ubyte.gz')

print("print image  ")

#-------------------------------------------------------
# step 3
# output image

image = Image.fromarray(np.array(trainImages[4444])) # python decompress and read it byte by byte into a data structures
image = image.convert('RGB')
image.show() # show image
image.save('train-4444-0.png') # save image in png file

image = Image.fromarray(np.array(trainImages[5555])) # python decompress and read it byte by byte into a data structures
image = image.convert('RGB')
image.show() # show image
image.save('train-5555-0.png') # save image in png file




      #  buffer = file.read(number_of_labels)
       # self.labels = np.frombuffer(buffer, astype (np.unit8))

   # images = []

        #print()
