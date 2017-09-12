import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup("Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    p = folium.Popup(str(el)+" m", parse_html=True)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=p,
                                     radius=5, color="grey", 
                                     fill_color=color_producer(el),
                                     fill_opacity=0.7, fill=True))
    # fg.add_child(folium.Marker(location=[lt, ln], popup=p, icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup("Poppulation")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                 style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
