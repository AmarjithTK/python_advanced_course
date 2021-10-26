



def ColorList(color_string):
    
    color_split = color_string.split(' ')
    for x in range(0,color_split.__len__()):
        temp = color_split[x]
        color_split[x] = int(temp)
    return color_split




