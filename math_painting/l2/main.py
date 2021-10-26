
from functions import ColorList
# from canvas import Canvas
# from shape import Rectangle,Square


from PIL import Image as ImageGen
import numpy as np


print("\nApp is launched , Now we can create the canvas  \n")
canvas_width_input = input('Enter the width of the canvas : ')
canvas_height_input = input('Enter the height of the canvas : ')
canvas_color_input = input('What color would you like the canvas to have ? black or white :')

canvas_color = [0,0,0] if canvas_color_input.upper() == 'BLACK' else [256,256,256]


canvas_sheet = np.zeros(shape=(int(canvas_height_input),int(canvas_width_input),3),dtype=np.uint8)
canvas_sheet[:] = canvas_color


print('A new canvas is successfully generated !')


while True:
    
    shape_input = input('What shape do you want to draw ? Rectangle or Square :')
    
    if(shape_input.upper() == 'RECTANGLE'):

        rect_x_input = input('Enter the x position of rectangle : ')
        rect_y_input = input('Enter the y position of rectangle : ')        
        rect_width_input = input('Enter the width of rectangle : ')
        rect_height_input = input('Enter the height of rectangle : ')
        rect_color_input = input('Enter the color of rectangle  "r  g  b" format :')        

        # rect = Rectangle(int(rect_width_input), int(rect_height_input), int(rect_x_input), int(rect_y_input), ColorList(rect_color_input))

        canvas_sheet[int(rect_y_input)-1:int(rect_y_input)-1+int(rect_height_input),int(rect_x_input)-1:int(rect_x_input)-1+int(rect_height_input)] = ColorList(rect_color_input)
        image  = ImageGen.fromarray(canvas_sheet,'RGB')
    
        

        q = input('Type q to quit and generate output file :')

    elif(shape_input.upper() == 'SQUARE'):

        sqr_x_input = input('Enter the x position of square : ')
        sqr_y_input = input('Enter the y position of square : ')        
        sqr_size_input = input('Enter the size of square : ')
        sqr_color_input = input('Enter the color of square  "r  g  b" format :')  

        # sqr = Square(int(sqr_size_input), int(sqr_x_input), int(sqr_y_input), ColorList(sqr_color_input))
        canvas_sheet[int(sqr_y_input)-1:int(sqr_y_input)-1+int(sqr_size_input)  ,    int(sqr_x_input)-1:int(sqr_x_input)-1+int(sqr_size_input)] = ColorList(sqr_color_input)
        image  = ImageGen.fromarray(canvas_sheet,'RGB')

        q = input('Type q to quit and generate output file :')

    else:
        print('Wrong selection !')
        continue

    if(q.upper() == 'Q'):
        print('Exiting the program')
        break    


image.save('canvas.png')
        








