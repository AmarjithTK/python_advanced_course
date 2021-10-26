import numpy as np
from PIL import Image as ImageGen



class Canvas:



    def __init__(self,width,height):
        self.canvas_plain = np.zeros(shape=(int(height),int(width),3),dtype=np.uint8)
        print('Canvas was created !')


        
    def GenerateCanvas(self,color):
        self.canvas_plain[:] = color
        print('Colored canvas was created !')
    
    def ExportCanvas(self):
        image  = ImageGen.fromarray(self.canvas_plain,'RGB')
        image.save('canvas.png')
        print('image')







