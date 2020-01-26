import  folium

map = folium.Map(location=[35.58,-99.09], zoom_start=6 , tiles="Stamen Terrain")

# user feature group 
fg = folium.FeatureGroup(name="My Map")

for Cord in [[35.58,-99.09],[35.58,-91.09],[35.58,-93.09],[35.58,-95.09],[35.58,-97.09]]:
    fg.add_child(folium.Marker(location=Cord,popup="Hello Marker",icon=folium.Icon(color='red')))


map.add_child(fg)
map.save("tilesTest3.html") 