import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# Define the base map function for India
def create_india_map():
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  # Centered on India
    # Create the base map centered on India with an initial zoom level
    folium_map = folium.Map(location=india_location, zoom_start=5)

    # Add zoom control and the default tile layer
    folium_map.add_child(folium.TileLayer("cartodb positron"))

    # Load GeoJSON data for Indian states
    with open('c:\Users\HP\Desktop\Python313\Lib\site-packages\geopandas\tests\data\null_geom.geojson\india_states.geojson') as f:
        india_states = json.load(f)

    # Add GeoJSON layer to the map with black borders
    folium.GeoJson(
        india_states,
        style_function=lambda feature: {
            'fillColor': 'transparent',
            'color': 'black',
            'weight': 2,
        }
    ).add_to(folium_map)

    return folium_map

# Create the map for India
map = create_india_map()

# Render the map in Streamlit
st_folium(map, width=725)
