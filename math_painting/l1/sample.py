import numpy as ns

from PIL import Image as ImageGen # generate a image from math


data_image = ns.zeros(shape=(5,10,3),dtype=ns.uint8) # blind numpy 3D array

data_image[:] = [255,255,255] # make image white


data_image[1:4:2,1:9] = [90,120,0] # make two patches [row1:row2:gap , column1:column2:gap]
            # :2 replace white with color for every 2nd pixel out of (1,2,3) - 1,3


image  = ImageGen.fromarray(data_image,'RGB')
image.save('canvas.png')
print(data_image)

