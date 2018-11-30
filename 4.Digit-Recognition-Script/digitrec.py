import gzip
from PIL import Image
import numpy as np

#self.name = name


#class MnistDataSet:
#def __init__(self, name, image_Path, lable_path):
   # self.name = name

    #self.parse_images(image_Path)
 #   self.parse_labels(lable_path)

#def parse_images(self, images_path):
def parse_images(images_path):
            
    with gzip.open(images_path, 'rb') as file:
        magic = int.from_bytes(file.read(4), 'big')
        #magic = int.from_bytes(file.read(4), 'big')
        print(" Magic number: " + str(magic))


        number_of_Images = int.from_bytes(file.read(4), 'big')
        print(" Number of Images: " + str(number_of_Images))


        rows = int.from_bytes(file.read(4), 'big')
        print(" Number of rows; " + str(rows))


        columns = int.from_bytes(file.read(4), 'big')
        print(" Number of Columns: " + str(columns))

       # buffer = file.read(rows * columns * number_of_Images)
       # data = np.frombuffer(buffer, dtype=np.uint8)
      #  self.images = data.reshape(number_of_Images, rows, columns)

        images = []
        for i in range(number_of_Images):
            rowss = []
            for r in range(rows):
                columnss = []
                for c in range(columns):
                    columnss.append(int.from_bytes(file.read(1), 'big'))
                rowss.append(columnss)
            images.append(rowss)
        return images

print()

trainImages = parse_images('train-images-idx3-ubyte.gz')
testImages = parse_images('t10k-images-idx3-ubyte.gz')




def parse_labels(labels_path):
    with gzip.open(labels_path, 'rb') as file:

        magic = int.from_bytes(file.read(4), 'big')
        print(" Magic number: " + str(magic))

        number_of_labels = int.from_bytes(file.read(4), 'big')
        print(" Number of labels: " + str(number_of_labels))

        labels =[file.read(1) for i in range(number_of_labels)]
        labels = [int.from_bytes(label, 'big') for label in labels]

        return labels

print()

translabels = parse_labels('train-labels-idx1-ubyte.gz')
testlabels = parse_labels('t10k-labels-idx1-ubyte.gz')

print("print image  ")

image = Image.fromarray(np.array(trainImages[750]))
image = image.convert('RGB')
image.show()
image.save('train-750-0.png')

#image = Image.fromarray(np.array(trainImages[5555]))
#image = image.convert('RGB')
#image.show()
#image.save('train-5555-0.png')




      #  buffer = file.read(number_of_labels)
       # self.labels = np.frombuffer(buffer, astype (np.unit8))

   # images = []

        #print()
