
# using datetime module vs date tuple

#  - Makes calculation much easier
#  - Can be easily manipulated

#  myDate = datetime(18,12,1988)
#  myEnd = datetime(30,12,2030)

#  age = myEnd - myDate
#  using tuples 

#  myDate = (12,12,2002)
#  myEnd = (19,10,2035)



# - Today date can be viewed by datetime.now()
# - Datetime class can be used method without needing a objectT



# Datetime function -
#  object identifier = Classname(arguments)


    # help(datetime.now)
    #     datetime.now required tz as the argument

# Timezone has to be object given as a argument


from folium import Map
from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform

class Geopoint:
    # init function is like the parameter definition of a class 
    
    def __init__(self,latitude,longitude): # parameters or argument goes here

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

india = Geopoint(latitude = '50.03', longitude = '43.33')
print(india.get_weather())









