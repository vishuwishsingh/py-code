import pandas as pd 
import folium 

file_data = pd.read_csv("Volcanoes.txt")

lat = list(file_data["LAT"])
lon = list(file_data["LON"])
elv = list(file_data["ELEV"])

map = folium.Map(location=[35.58,-99.09], zoom_start=6 , tiles="Stamen Terrain")

# user feature group 
fg = folium.FeatureGroup(name="My Map")

for la , lo , el in zip(lat , lon , elv):
    fg.add_child(folium.Marker(location=[la,lo],popup=str(el)+" m" ,icon=folium.Icon(color='red')))


map.add_child(fg)
map.save("tilesTest4.html") 
