from folium import Map



# anti pode means opposite site of the earth coordinates

# for latitude we need to multiply with -1 so that we get antipode. 
# for longitude given it is positive then subtract 180 degrees to get the antipode


# latitude and longitude are referenced using center of earth and equator as reference 
 
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


maplist = list((antipode_latitude, antipode_longitude))


myMap = Map(maplist)
myMap.save(str('map.html'))



print(antipode_latitude)
print(antipode_longitude)