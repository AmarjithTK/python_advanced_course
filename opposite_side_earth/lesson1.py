# ***** Low - Level working of python demonstrating program

from folium import Map
  

# ** anti pode means opposite site of the earth coordinates
# ** for latitude we need to multiply with -1 so that we get antipode. 
# ** for longitude given it is positive then subtract 180 degrees to get the antipode
# ** latitude and longitude are referenced using center of earth and equator as reference 
 
latitude=float("50.04")
longitude=float("39.94")


antipode_latitude = latitude.__mul__(int("-1"))

if longitude.__lt__(float("0")):
    antipode_longitude = longitude.__add__(float('180'))
elif longitude.__eq__(float("0")):
# location is the reference point    
    antipode_longitude = float('180')
elif longitude.__gt__(float("180")) or longitude.__lt__(float("-180")):

# longitude is more than what it should be
    antipode_longitude = str('invalid longitude detected')        
else:
    antipode_longitude = longitude.__sub__(float('180'))


maplist = list((antipode_latitude, antipode_longitude)) # creates a list with two variables


myMap = Map(maplist)
myMap.save(str('map.html')) # outputs the map with antipode coordinates into an html file



# More readable python code implementation of this program can be done with 

# addition by using -  '+'
# subtraction by - '-'
# multiplication by - '*'
# less than by - '<'
# less than or equal to by - '<='
# equal to by - '=='
# float('40.458') by just 40.458
# if longitude <=0 :
# location = list((a,b)) by location = [a,b]
# str('')  by just ''


# ================ The Nine elements of python =========================

# 1) class is used to define object in programming languages
# objects in this code :
# folium,Map,float,int,str,list,__add__,__eq__,__gt__,__lt__,__mul__,__sub__,Map.save
# ----------------------

# 2) identifiers (variables) in this code :
# latitude,longitude,antipode_longitude,antipode_latitude
# -----------------------

# 3) keywords are reserved words in python ,  These keywords cannot be used as an identifiers
# for , import , if , else , elif
# -----------------------

# 4) Delimiters are the special characters
#     = , "" , () , . ,
# -----------------------

# 5) Blank spaces - blank spaces between the lines of code . Used to seperate code blocks
# -----------------------

# 6) White spaces - white spaces between from <--> folium <--> import this can be as much as we want 
# -----------------------

# 7) indentation - you know what is this
# -----------------------

# 8) comments - what is this then ?
# -----------------------

# 9) Operators -  '+ , - , * , <= , >= , '



# +++ Type function gives the type of a class and more information


print(antipode_latitude) # nothing to see here
print(antipode_longitude)


