from folium.features import ColorLine
from geopy.geocoders import Nominatim
#from folium import Map
# from folium import plugins
import folium


geolocator = Nominatim(user_agent="Neoapptest")
direccion="Manuela Pedraza 2675, Mar del Plata, Argentina"
lugar = geolocator.geocode(direccion)
print(lugar.address)
print(lugar.latitude)
print (lugar.longitude)
coordenadas=str(lugar.latitude)+str(lugar.longitude)
#mapa=folium.Map location=[location.latitude,location.longitude]
mapa=folium.Map (location=[lugar.latitude,lugar.longitude],width=600,height=600, tiles='OpenStreetMap',zoom_start=11,contro_scale=True)
# lugar=Marker (location=[lugar.latitude,lugar.longitude])
folium.Marker(location=[lugar.latitude,lugar.longitude],popup=direccion,tooltip=coordenadas,icon=folium.Icon(color="green")).add_to(mapa)
folium.Circle (location=[lugar.latitude,lugar.longitude],radius=30000,fill=True).add_to(mapa)
mapa.save ('mapa.html')

