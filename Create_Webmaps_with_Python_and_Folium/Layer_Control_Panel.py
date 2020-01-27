import pandas as pd 
import folium 

file_data = pd.read_csv("Volcanoes.txt")

lat = list(file_data["LAT"])
lon = list(file_data["LON"])
elv = list(file_data["ELEV"])

def Marker_color(eleviation):
    if eleviation <= 1000:
        return 'green'
    elif eleviation > 1000 and eleviation <= 3000 :
        return 'orange'
    else:
        return 'red'
        

map = folium.Map(location=[35.58,-99.09], zoom_start=6 , tiles="Stamen Terrain")

# user feature group 
fgv = folium.FeatureGroup(name="Volcanoes")

for la , lo , el in zip(lat , lon , elv):
    fgv.add_child(folium.CircleMarker(location=[la,lo],radius=6, popup=str(el)+" m", fill_color= Marker_color(el) , color = 'grey' , fill=True , fill_opacity =0.7  ))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("tilesTest9.html") 


