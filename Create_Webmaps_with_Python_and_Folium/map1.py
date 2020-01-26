import  folium

map = folium.Map(location=[35.58,-99.09], zoom_start=6 , tiles="Stamen Terrain")
#map.add_child(folium.Marker(location=[35.58,-99.09],popup="Hi I am Marker" , icon=folium.Icon(color='blue')))

# user feature group 
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[35.58,-99.09],popup="Hello Marker",icon=folium.Icon(color='red')))
map.add_child(fg)

#map.save("tilesTest1.html") 
map.save("tilesTest2.html") 