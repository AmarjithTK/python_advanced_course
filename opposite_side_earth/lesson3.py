# ========== Inheritance | Lesson - 3 ===============


# using methods defined on the Marker class and inheriting those methods into geopoint class


# Inheritance help us to take methods of other class to the required class

#  - Here we are going to inherit methods of Marker class to Geopoint class 
#  - This helps us to use '.add_to ' method from 'Marker' class in the 'Geopoint'



from folium import Map,Popup
from lesson3geo import Geopoint

latitude = '50.3'
longitude = '30.22'


#  Geopoint instance
geopoint  =  Geopoint(latitude = latitude , longitude = longitude)

# we can add popup argument here if we wish using inherited arguments 

lesson3 : Inheritance of class methods and arguments

 - Inherited methods of different classes to Geopoint
 - add_to method of adding elements to objects
 - added popup with weather details list converted to string
 - inherited variables and inherited methods



popup = Popup(str(geopoint.get_weather()))

#   Here the list is converted to str because Popup method only accepts html or string as input
#   Argument here is 'html' = either string  or Element content of popup


# Popup instance created
popup.add_to(geopoint)

# Map instance created 
mymap = Map(location = [latitude, longitude])



geopoint.add_to(mymap)


mymap.save('map.html')





