
  
 
latitude=50.04
longitude=39.94


antipode_latitude = latitude * -1

if longitude < 0:
    antipode_longitude = longitude +180
elif longitude ==  0:
# location is the reference point    
    antipode_longitude = 180
elif longitude >= 180 or longitude <= -180 :

# longitude is more than what it should be
    antipode_longitude = invalid longitude detected      
else:
    antipode_longitude = longitude - 180


maplist = [antipode_latitude, antipode_longitude] # creates a list with two variables


myMap = Map(maplist)
myMap.save('map.html') # outputs the map with antipode coordinates into an html file

