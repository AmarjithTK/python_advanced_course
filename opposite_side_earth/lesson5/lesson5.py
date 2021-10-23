from folium import Map,Marker,Popup
from random import uniform
from lesson5geo import Geopoint





mymap = Map(location= [55,44])























for x in range(1,100):
    lat = uniform(-90,90)
    lon = uniform(-180,180)
    india = Geopoint(lat,lon)
    forecast_data=india.get_weather()
    popup_string = '<div style="width:100%;height:20px;margin:50px 0;background-color:red;"></div><h1 style="text-align:center;color:blue;margin:20px auto;">Weather Map </h1>'
    for i in range(0,forecast_data.__len__()):
        popup_string += f"""{forecast_data[i][0][-8:]} - Time \t {((forecast_data[i][1])*(5/9))-32} - Temp \t {forecast_data[i][2]} - Weather <hr width = 5>"""
    popup = Popup(popup_string,max_width=500)
    popup.add_to(india)
    india.add_to(mymap)





mymap.save('map.html')




# ---- Self attempt code ----

# for x in range(1,50):
#     lat = uniform(-90,90)
#     lon = uniform(-180,180)
#     locale = Marker(location=[lat,lon])
#     locale.add_to(mymap)


# for val in forecast_data:
#     print(val[0],'indicator')

# print(forecast_data[0][0][-8:])
# # print(forecast_data[0][0][-1])

# print('\n',forecast_data[0][0])

#     locale = Marker(location=[lat,lon])
#     locale.add_to(mymap)