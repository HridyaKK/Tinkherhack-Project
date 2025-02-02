import json
import folium
import streamlit as st
from streamlit_folium import st_folium

# Define the base map function for India with added effects
def create_india_map(highlight_states=[], highlight_color='yellow', highlight_border_color='red', zoom_level=5, opacity=0.7):
    india_location = [20.5937, 78.9629]  # Centered on India
    folium_map = folium.Map(location=india_location, zoom_start=zoom_level, control_scale=True)
    
    folium_map.add_child(folium.TileLayer("cartodb positron"))
   
    with open(r'C:\Users\HP\Desktop\Tinkherhack\Indian_States.json') as f:
        india_states = json.load(f)
    
    # Define custom styling for the GeoJSON layer
    geojson_layer = folium.GeoJson(
        india_states,
        style_function=lambda feature: {
            'fillColor': highlight_color if feature['properties'].get('NAME_1') in highlight_states else 'transparent',
            'color': highlight_border_color if feature['properties'].get('NAME_1') in highlight_states else 'black',
            'weight': 2,
            'dashArray': '5, 5' if feature['properties'].get('NAME_1') in highlight_states else '0',
            'fillOpacity': opacity,  # Add opacity to the color fill
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
        }  # Add effects on hover (e.g., increased border weight and fill opacity)
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
highlight_border_color = 'red'

if main_option == "Crops":
    show_c
