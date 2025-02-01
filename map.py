import streamlit as st
import folium
from streamlit_folium import st_folium
import json
import os



# Function to get the coordinates of Kerala
def get_kerala_coordinates():
    return [10.8505, 76.2711]  # Coordinates for Kerala

# Define the base map function for India
def create_india_map(highlight_kerala=False):
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
            'fillColor': 'yellow' if highlight_kerala and feature['properties'].get('NAME_1') == 'Kerala' else 'transparent',
            'color': 'black' if feature['properties'].get('NAME_1') != 'Kerala' else 'red',
            'weight': 2,
        }
    ).add_to(folium_map)
    # Fit the map to the bounds of the GeoJSON layer
    folium_map.fit_bounds(geojson_layer.get_bounds())
    # Zoom to Kerala if specified
    if highlight_kerala:
        kerala_coords = get_kerala_coordinates()
        folium_map.set_view(kerala_coords, zoom=7)
        folium.Marker(kerala_coords, tooltip="Kerala").add_to(folium_map)
    return folium_map

# Add checkboxes for main options
st.sidebar.header("Options")
show_crops = st.sidebar.checkbox("Crops")
show_rivers = st.sidebar.checkbox("Rivers")
show_coal = st.sidebar.checkbox("Coal")

# Add sub-options for Crops
highlight_kerala = False
if show_crops:
    with st.sidebar.expander("Crops Options"):
        show_rice = st.checkbox("Rice")
        show_wheat = st.checkbox("Wheat")
        show_ragi = st.checkbox("Ragi")
        if show_ragi:
            highlight_kerala = True

# Create the map for India
map = create_india_map(highlight_kerala=highlight_kerala)

# Render the map in Streamlit
st_folium(map, width=725)

# You can add logic here to display additional layers or information based on the selected options
# if show_rice:
#     st.write("Displaying Rice data...")
#     # Add code to display Rice data on the map

# if show_wheat:
#     st.write("Displaying Wheat data...")
#     # Add code to display Wheat data on the map

# if show_ragi:
#     st.write("Displaying Ragi data...")
#     # Add code to display Ragi data on the map

if show_rivers:
    st.write("Displaying Rivers data...")
    # Add code to display Rivers data on the map

if show_coal:
    st.write("Displaying Coal data...")
    # Add code to display Coal data on the map
