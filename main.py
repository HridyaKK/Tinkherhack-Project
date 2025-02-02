
import json
import folium
import streamlit as st
from streamlit_folium import st_folium

# Define the base map function for India with added effects
def create_india_map(highlight_states=[], highlight_color='yellow', highlight_border_color='red'):
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  
    # Create the base map 
    folium_map = folium.Map(location=india_location, zoom_start=5)
    
    folium_map.add_child(folium.TileLayer("cartodb positron"))
   
    import os
    import json


    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    file_path = os.path.join(script_dir, 'Indian_States.json')

    with open(file_path) as f:
        india_states = json.load(f)

    # Define custom styling for the GeoJSON layer
    geojson_layer = folium.GeoJson(
        india_states,
        style_function=lambda feature: {
            'fillColor': highlight_color if feature['properties'].get('NAME_1') in highlight_states else 'transparent',
            'color': highlight_border_color if feature['properties'].get('NAME_1') in highlight_states else 'black',
            'weight': 2,
            'dashArray': '5, 5' if feature['properties'].get('NAME_1') in highlight_states else '0',
            'fillOpacity': 0.7, 
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME_1'],
            aliases=['State:'],
            style=("background-color: black; color: white; font-style: italic;")
        ),
        highlight_function=lambda feature: {
            'weight': 3,
            'color': 'blue',
            'fillOpacity': 0.9
        }  # Add effects on hover 
    ).add_to(folium_map)

    folium_map.fit_bounds(geojson_layer.get_bounds())
    return folium_map

# Add the main radio button for selecting options
st.sidebar.header("Options")
main_option = st.sidebar.radio("Select one option", ["Crops", "Mountains", "Soil"])

# Logic based on the selected main option
highlight_states = []
highlight_color = 'yellow'
highlight_border_color = 'red'

if main_option == "Crops":
    show_crops = True
    with st.sidebar.expander("Crops Options"):
        crop_option = st.radio("Select a crop", ["Rice", "Wheat", "Ragi", "Sugarcane", "Maize"])
        if crop_option == "Ragi":
            highlight_states = ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"]
            highlight_color = '#752b2b'
            highlight_border_color = '#451a1a'
        elif crop_option == "Rice":
            highlight_states = ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"]
            highlight_color = '#d6c3c3'
            highlight_border_color = '#736b6b'
        elif crop_option == "Wheat":
            highlight_states = ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
            highlight_color = '#ba9e2f'
            highlight_border_color = '#d6660b'
        elif crop_option == "Sugarcane":
            highlight_states = ["Maharashtra", "Uttar Pradesh", "Karnataka", "Andhra Pradesh"]
            highlight_color = 'lightgreen'
            highlight_border_color = 'darkgreen'
        elif crop_option == "Maize":
            highlight_states = ["Madhya Pradesh", "Rajasthan", "Karnataka"]
            highlight_color = 'lightblue'
            highlight_border_color = 'darkblue'

elif main_option == "Mountains":
    show_mountains = True
    with st.sidebar.expander("Mountain Options"):
        mountain_option = st.radio("Select a mountain range", ["Himalayas", "Western Ghats", "Eastern Ghats"])
        if mountain_option == "Himalayas":
            highlight_states = ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"]
            highlight_color = 'lightblue'
            highlight_border_color = 'blue'
        elif mountain_option == "Western Ghats":
            highlight_states = ["Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu"]
            highlight_color = 'lightgreen'
            highlight_border_color = 'green'
        elif mountain_option == "Eastern Ghats":
            highlight_states = ["Odisha", "Andhra Pradesh", "Tamil Nadu"]
            highlight_color = 'orange'
            highlight_border_color = 'darkorange'

elif main_option == "Soil":
    show_soil = True
    with st.sidebar.expander("Soil Options"):
        soil_option = st.radio("Select a soil type", ["Alluvial", "Red Soil", "Arid", "Clayey", "Peaty"])
        if soil_option == "Alluvial":
            highlight_states = ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal"]
            highlight_color = 'lightyellow'
            highlight_border_color = 'gold'
        elif soil_option == "Red Soil":
            highlight_states = ["Chhattisgarh", "Orissa"]
            highlight_color = 'red'
            highlight_border_color = 'darkred'
        elif soil_option == "Arid":
            highlight_states = ["Gujarat", "Haryana"]
            highlight_color = '#c2ac9b'
            highlight_border_color = 'brown'
        elif soil_option == "Clayey":
            highlight_states = ["Chhattisgarh", "Malwa"]
            highlight_color = 'darkgrey'
            highlight_border_color = 'grey'
        elif soil_option == "Peaty":
            highlight_states = ["Kerala", "West Bengal"]
            highlight_color = 'darkgreen'
            highlight_border_color = 'green'

# Create the map for India with the selected options
map = create_india_map(highlight_states=highlight_states, highlight_color=highlight_color, highlight_border_color=highlight_border_color)

# Render the map in Streamlit
st_folium(map, width=725)
