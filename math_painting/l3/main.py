from canvas import Canvas
from shape import Rectangle,Square,ColorList




width = input('Enter width of canvas : ')
height = input('Enter height of canvas : ')
color = input('Enter color of canvas ? white or black : ')

canvas_color = [0,0,0] if color.upper() =='BLACK' else [250,250,250]
canvas=Canvas(height,width,canvas_color)


while True:
    
    shape_input = input('What shape do you want to draw ? Rectangle or Square :')
    
    if(shape_input.upper() == 'RECTANGLE'):
        x = input('Enter the x position of rectangle : ')
        y = input('Enter the y position of rectangle : ')        
        a = input('Enter the width of rectangle : ')
        b = input('Enter the height of rectangle : ')
        rectcol = input('Enter the color of rectangle  "r  g  b" format : ')        
        rect =Rectangle(x, y, a, b, ColorList(rectcol))
        rect.Draw(canvas)
        q = input('Type q to quit and generate output file : ')

    elif(shape_input.upper() == 'SQUARE'):

        x = input('Enter the x position of square : ')
        y = input('Enter the y position of square : ')        
        a = input('Enter the size of square : ')
        sqrcol = input('Enter the color of square  "r  g  b" format : ')  
        sqr = Square(x, y, a, ColorList(sqrcol))
        sqr.Draw(canvas)
        q = input('Type q to quit and generate output file : ')


    else:
        print('Wrong selection !')
        continue

    if(q.upper() == 'Q'):
        print('Exiting the program')
        break    

canvas.generateImage()