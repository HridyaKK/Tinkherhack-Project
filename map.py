import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os

# Function to get the coordinates of Kerala
def get_kerala_coordinates():
    return [10.8505, 76.2711]  # Coordinates for Kerala

# Define the base map function for India
def create_india_map(highlight_states=[]):
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  # Centered on India
    # Create the base map centered on India with an initial zoom level
    folium_map = folium.Map(location=india_location, zoom_start=5)
    # Add zoom control and the default tile layer
    folium_map.add_child(folium.TileLayer("cartodb positron"))
    # Load GeoJSON data for Indian states
    current_dir = os.path.dirname(os.path.abspath(__file__))
    geojson_path = os.path.join(current_dir, 'Indian_States.json')
    with open(geojson_path) as f:
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
        show_rice = st.checkbox("Rice")
        show_wheat = st.checkbox("Wheat")
        show_ragi = st.checkbox("Ragi")
        if show_ragi:
            highlight_states = ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"]
        elif show_rice:
            highlight_states = ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"]
        elif show_wheat:
            highlight_states = ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
elif main_option == "Rivers":
    show_rivers = True
elif main_option == "Soil":
    show_soil = True
    with st.sidebar.expander("Soil Options"):
        show_alluvial = st.checkbox("Alluvial")
        show_red_soil = st.checkbox("Red Soil")
        show_arid = st.checkbox("Arid")
        show_clayey = st.checkbox("Clayey")

# Create the map for India
map = create_india_map(highlight_states=highlight_states)

# Render the map in Streamlit
st_folium(map, width=725)

# Additional layers based on the selected options
if show_crops:
    if show_rice:
        st.write("Displaying Rice data...")
        # Add code to display Rice data on the map

    if show_wheat:
        st.write("Displaying Wheat data...")
        # Add code to display Wheat data on the map

    if show_ragi:
        st.write("Displaying Ragi data...")
        # Add code to display Ragi data on the map

if show_rivers:
    st.write("Displaying Rivers data...")
    # Add code to display Rivers data on the map

if show_soil:
    st.write("Displaying Soil data...")
    # Add code to display Soil data on the map