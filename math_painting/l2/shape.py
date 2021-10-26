
class Rectangle:

    def __init__(self,width,height,x,y,color):
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.color=color

    def Add(self,canvas):

        canvas[self.y-1:self.y-1+self.height,self.x-1:self.x-1+width] = self.color

class Square:

    def __init__(self,size,x,y,color):
        self.size
        self.x=x
        self.y=y
        self.color=color

    def Add(self,canvas):

        canvas[self.y-1:self.y-1+self.size,self.x-1:self.x-1+self.size] = self.color


# Artifical do-while loop for python
