
import json
import folium
import streamlit as st
from streamlit_folium import st_folium

# Define the base map function for India
def create_india_map(highlight_states=[], highlight_color='yellow'):
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  # Centered on India
    # Create the base map centered on India with an initial zoom level
    folium_map = folium.Map(location=india_location, zoom_start=5)
    # Add zoom control and the default tile layer
    folium_map.add_child(folium.TileLayer("cartodb positron"))
   
    with open(r'C:\Users\HP\Desktop\Tinkherhack\Indian_States.json') as f:
        india_states = json.load(f)
    # Add GeoJSON layer to the map with black borders
    geojson_layer = folium.GeoJson(
        india_states,
        style_function=lambda feature: {
            'fillColor': highlight_color if feature['properties'].get('NAME_1') in highlight_states else 'transparent',
            'color': 'black' if feature['properties'].get('NAME_1') not in highlight_states else 'red',
            'weight': 1.5,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME_1'],
            aliases=['State:'],
            style=("background-color: black; color: white; font-style: italic;")
        )
    ).add_to(folium_map)
    # Fit the map to the bounds of the GeoJSON layer
    folium_map.fit_bounds(geojson_layer.get_bounds())
    return folium_map

# Add the main radio button for selecting options
st.sidebar.header("Options")
main_option = st.sidebar.radio("Select one option", ["Crops", "Mountains", "Soil"])
# Logic based on the selected main option
highlight_states = []
highlight_color = 'yellow'
show_crops = False
show_rivers = False
show_soil = False

if main_option == "Crops":
    show_crops = True
    with st.sidebar.expander("Crops Options"):
        crop_option = st.radio("Select a crop", ["Rice", "Wheat", "Ragi"])
        if crop_option == "Ragi":
            highlight_states = ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"]
            highlight_color = 'coffee'
        elif crop_option == "Rice":
            highlight_states = ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"]
            highlight_color = 'grey'
        elif crop_option == "Wheat":
            highlight_states = ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
            highlight_color = 'yellow'
elif main_option == "Mountains":
    show_mountains = True
    with st.sidebar.expander("Mountain Options"):
        mountain_option = st.radio("Select a mountain range", ["Himalayas", "Western Ghats", "Eastern Ghats"])
        if mountain_option == "Himalayas":
            highlight_states = ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"]
            highlight_color = 'blue'
        elif mountain_option == "Western Ghats":
            highlight_states = ["Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu"]
            highlight_color = 'green'
        elif mountain_option == "Eastern Ghats":
            highlight_states = ["Odisha", "Andhra Pradesh", "Tamil Nadu"]
            highlight_color = 'orange'

    
elif main_option == "Soil":
    show_soil = True
    with st.sidebar.expander("Soil Options"):
        soil_option = st.radio("Select a soil type", ["Alluvial", "Red Soil", "Arid", "Clayey"])
        if soil_option == "Alluvial Soil":
            highlight_states = ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal"]
        elif soil_option == "Red Soil":
            highlight_states = ["Chhattisgarh", "Orissa"]
        elif soil_option == "Arid":
            highlight_states = ["Gujarat", "Haryana"]
        elif soil_option == "Clayey":
            highlight_states = ["Chhattisgarh", "Malwa"]

# Create the map for India
map = create_india_map(highlight_states=highlight_states, highlight_color=highlight_color)

# Render the map in Streamlit
st_folium(map, width=725)

