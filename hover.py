
#hover effects
import folium

# Create a map centered on India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add a marker with a tooltip (hover effect)
folium.Marker([20.5937, 78.9629], 
              popup="This is a crop area", 
              tooltip="Hover over me!").add_to(m)

# Display the map
from streamlit_folium import st_folium
st_folium(m, width=700, height=500)
import folium
import geopandas as gpd

# Example GeoJSON data for a region (you can replace it with your actual GeoJSON data)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [78.9629, 20.5937],
                        [79.9629, 20.5937],
                        [79.9629, 21.5937],
                        [78.9629, 21.5937]
                    ]
                ]
            },
            "properties": {"name": "Crop Area"}
        }
    ]
}

# Create a map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Define style for GeoJSON highlight
style_function = lambda x: {
    'fillColor': '#ff0000',
    'color': 'black',
    'weight': 2,
    'fillOpacity': 0.5
}

# Create GeoJSON layer with hover functionality
folium.GeoJson(
    geojson_data,
    name="Crops",
    style_function=style_function,
    highlight_function=lambda x: {'weight': 5, 'fillOpacity': 0.7}  # Highlight effect
).add_to(m)

# Add a marker with popup for context
folium.Marker([20.5937, 78.9629], popup="Crop Region").add_to(m)

# Display the map
from streamlit_folium import st_folium
st_folium(m, width=700, height=500)
import folium
from streamlit_folium import st_folium
import streamlit as st

# Sidebar selection to toggle between layers
selected_layer = st.sidebar.selectbox("Select a layer to display", ["Crops", "Mines", "Water Bodies"])

# Create a map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Conditional logic to add different layers
if selected_layer == "Crops":
    folium.Marker([20.5937, 78.9629], popup="Crops Area").add_to(m)
elif selected_layer == "Mines":
    folium.Marker([20.5937, 79.9629], popup="Mines Area").add_to(m)
elif selected_layer == "Water Bodies":
    folium.Marker([21.5937, 78.9629], popup="Water Body").add_to(m)

# Display map
st_folium(m, width=700, height=500)

