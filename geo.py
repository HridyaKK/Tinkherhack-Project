import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st

geo_data_crops = gpd.read_file('C:/Users/jiyaj/OneDrive/Desktop/python s1/crops_data.geojson')
geo_data_crops = gpd.read_file('C:/Users/jiyaj/OneDrive/Desktop/python s1/soil_data.geojson')


# Load GeoJSON data (replace with your actual file paths)
geo_data_crops = gpd.read_file('crops_data.geojson')
geo_data_soils = gpd.read_file('soil_data.geojson')

# Create a base map centered on India or any location
base_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Create separate layers for crops and soils
crop_layer = folium.FeatureGroup(name="Crops")
soil_layer = folium.FeatureGroup(name="Soils")

# Add GeoJSON data to the respective layers
folium.GeoJson(geo_data_crops).add_to(crop_layer)
folium.GeoJson(geo_data_soils).add_to(soil_layer)

# Add layers to the map
crop_layer.add_to(base_map)
soil_layer.add_to(base_map)

# Add Layer Control to toggle layers on and off
folium.LayerControl().add_to(base_map)

# Display the map in Streamlit
folium_static(base_map)
