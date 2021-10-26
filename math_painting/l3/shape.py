import numpy as np

# a= width b =height

class Rectangle:
    def __init__(self,x,y,a,b,color):
        self.x =int(x) 
        self.y=int(y)
        self.a=int(a)
        self.b=int(b)
        self.color=color
    def Draw(self,canvas):
        print(type(canvas.data))
        canvas.data[self.y-1:self.y-1+self.b , self.x-1:self.x-1+self.a] = self.color
        # canvas.data[self.y-1:self.y-1+self.b , self.x-1:self.x-1+self.a] = [0,0,0]
        print(canvas.data)
        # 5 5 5 5
        # 4:9, 4:9
        # 4 5 6 7 8 9  4 5 6 7 8 9

class Square:
    def __init__(self,x,y,a,color):
        self.x =int(x) 
        self.y=int(y)
        self.a=int(a)
        self.color=color
    def Draw(self,canvas):
        canvas.data[self.y-1:self.y-1+self.a , self.x-1:self.x-1+self.a] = self.color

def ColorList(color_string):
    
    color_split = color_string.split(' ')
    for x in range(0,color_split.__len__()):
        temp = color_split[x]
        color_split[x] = int(temp)
    return color_split