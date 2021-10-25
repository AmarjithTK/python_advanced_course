
from folium import Map,Marker
from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform

class Geopoint(Marker):

    # # add_to method
    # #geopoint.add_to(mymap)  -------------- what will be added ???.
    # Marker inside the geopoint class will be added to mymap........... concept clear ???

    # **geopoint.add_to is doing Marker.add_to(mymap)








    # init function is like the parameter definition of a class 
    
    def __init__(self,latitude,longitude,popup=None):
         # parameters or argument goes here
        super().__init__(location= [latitude,longitude],popup=popup)
        self.longitude = longitude
        self.latitude = latitude

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude,lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))

    def get_weather(self):

       
        weather = Weather(apikey = "ceb136a127a42a0e8c1d341e302161a0", lat = self.latitude,lon = self.longitude)
        # print(weather.next_12h_simplified())
        return weather.next_12h_simplified()


    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90,90), longitude = uniform(-180,180))   