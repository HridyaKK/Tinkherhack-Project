import os
import json
import csv
import folium
import streamlit as st
from streamlit_folium import st_folium

# Function to read locations from CSV file
def read_locations_from_csv(filename):
    locations = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            locations.append({
                "name": row["name"],
                "latitude": float(row["latitude"]),
                "longitude": float(row["longitude"])
            })
    return locations

# Define the base map function for India
def create_india_map(highlight_states=[], locations=[]):
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  # Centered on India
    # Create the base map centered on India with an initial zoom level
    folium_map = folium.Map(location=india_location, zoom_start=5)
    # Add zoom control and the default tile layer
    folium_map.add_child(folium.TileLayer("cartodb positron"))
    
    # Load GeoJSON data for Indian states
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(current_dir, 'Indian_States.json')
    with open(r'C:\Users\HP\Desktop\Tinkherhack\Indian_States.json') as f:
        india_states = json.load(f)
    
    # Add GeoJSON layer to the map with black borders
    geojson_layer = folium.GeoJson(
        india_states,
        style_function=lambda feature: {
            'fillColor': 'yellow' if feature['properties'].get('NAME_1') in highlight_states else 'transparent',
            'color': 'black' if feature['properties'].get('NAME_1') not in highlight_states else 'red',
            'weight': 2,
        }
    ).add_to(folium_map)
    
    # Add markers for locations read from CSV file
    for loc in locations:
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            popup=folium.Popup(f"Location: {loc['name']}", max_width=300)
        ).add_to(folium_map)
    
    # Fit the map to the bounds of the GeoJSON layer
    folium_map.fit_bounds(geojson_layer.get_bounds())
    
    return folium_map

# Add the main radio button for selecting options
st.sidebar.header("Options")
main_option = st.sidebar.radio("Select one option", ["Crops", "Rivers", "Soil"])

# Logic based on the selected main option
highlight_states = []

if main_option == "Crops":
    show_crops = True
    with st.sidebar.expander("Crops Options"):
        crop_option = st.radio("Select a crop", ["Rice", "Wheat", "Ragi"])
        if crop_option == "Ragi":
            highlight_states = ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"]
        elif crop_option == "Rice":
            highlight_states = ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"]
        elif crop_option == "Wheat":
            highlight_states = ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
elif main_option == "Rivers":
    show_rivers = True
elif main_option == "Soil":
    show_soil = True
    with st.sidebar.expander("Soil Options"):
        soil_option = st.radio("Select a soil type", ["Alluvial", "Red Soil", "Arid", "Clayey"])
        if soil_option == "Red Soil":
            highlight_states = ["Chhattisgarh", "Orissa"]
        elif soil_option == "Arid":
            highlight_states = ["Gujarat", "Haryana"]
        elif soil_option == "Clayey":
            highlight_states = ["Chhattisgarh", "Malwa"]

# Read the CSV file to get locations
filename = "latitude_longitude.csv"  # Make sure this matches the CSV you created
locations = read_locations_from_csv(filename)

# Create the map for India with CSV data and selected states
map = create_india_map(highlight_states=highlight_states, locations=locations)

# Render the map in Streamlit
st_folium(map, width=725)

# Additional layers based on the selected options
if show_crops:
    st.write(f"Displaying {crop_option} data...")

if show_rivers:
    st.write("Displaying Rivers data...")

if show_soil:
    st.write(f"Displaying {soil_option} data...")
