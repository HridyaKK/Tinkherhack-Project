import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st

import json

# Sample crop data with latitude and longitude
crop_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"crop": "Wheat"},
            "geometry": {
                "type": "Point",
                "coordinates": [78.9629, 20.5937]
            }
        },
        {
            "type": "Feature",
            "properties": {"crop": "Rice"},
            "geometry": {
                "type": "Point",
                "coordinates": [85.324, 27.7172]
            }
        }
    ]
}

# Save as a GeoJSON file
with open("crops_data.geojson", "w") as file:
    json.dump(crop_data, file)

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


import csv

# Function to create a CSV file with latitude and longitude data
def create_lat_long_csv(filename):
    data = [
        {"name": "Region A", "latitude": 12.9716, "longitude": 77.5946},
        {"name": "Region B", "latitude": 28.7041, "longitude": 77.1025},
        {"name": "Region C", "latitude": 19.0760, "longitude": 72.8777},
    ]
    
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "latitude", "longitude"])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV file '{filename}' created successfully.")

# Create the CSV file
filename = "latitude_longitude.csv"
create_lat_long_csv(filename)

# Read the CSV file and extract latitude and longitude data
locations = []
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        locations.append({
            "name": row["name"],
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"])
        })

# Create a map centered at the first location
m = folium.Map(location=[locations[0]["latitude"], locations[0]["longitude"]], zoom_start=6)

# Define layer colors
layer_colors = {
    "Crops": "green",
    "Mines": "gray",
    "Water Bodies": "blue",
    "Soil": "brown"
}

# Add markers for each location
for loc in locations:
    folium.Marker(
        location=[loc["latitude"], loc["longitude"]],
        popup=folium.Popup(f"Location: {loc['name']}", max_width=300)
    ).add_to(m)

folium.LayerControl().add_to(m)

# Save map as an HTML file
m.save("map.html")
print("Map has been created successfully!")
import streamlit as st

st.components.v1.html(open("map.html", "r").read(), height=600)


