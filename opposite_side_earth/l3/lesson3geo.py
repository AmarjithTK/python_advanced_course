# ========= Using inherited methods and variables  =========




    #   class class_name(parent_class):


    #       def __init__(self, arg1 , arg2 , arg3):

    #         super().__init__(arguments)  -----> Initialised the parent methods

    #         self.arg1 = arg1
    #         self.arg2 = arg2
    #         self.arg3 = arg3



from folium import Map
from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):
    # init function is like the parameter definition of a class 
    
    def __init__(self,latitude,longitude, popup=None): # popup parameter is defined inside Geopoint
        
        
        # Why there is a [ popup = None ] value assigned with it
        # That is because popup is a required argument and if the user dont provide a valid
        # Argument then the program will give complete error even though it could easily run without a popup displayed
        # [ popup = None ] fixes that problem by giving the argument with an empty value 
        # Even though it is empty, It's presence will make program work without crashes

        
        # init the object


        super().__init__(location = [latitude,longitude],popup = popup) # this will create a inheritance


        self.longitude = longitude
        self.latitude = latitude




    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude,lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))




    def get_weather(self):      
        weather = Weather(apikey = "ceb136a127a42a0e8c1d341e302161a0", lat = self.latitude,lon = self.longitude)
        return weather.next_12h_simplified()




    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90,90), longitude = uniform(-180,180))  
















