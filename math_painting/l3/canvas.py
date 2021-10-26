import numpy as np
from PIL import Image





class Canvas:
    def __init__(self,height,width,color):
        self.height=int(height)
        self.width=int(width)
        self.data = np.zeros(shape=(self.height,self.width,3),dtype=np.uint8)
        self.data[:]=color
    # def updateCanvas()    

    def generateImage(self):
        img = Image.fromarray(self.data,'RGB')
        img.save('canvas.png')