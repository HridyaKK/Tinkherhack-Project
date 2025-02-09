import json
import folium
import streamlit as st
from streamlit_folium import st_folium
import os
from functools import lru_cache

# Cache the JSON loading to prevent repeated file reads
@lru_cache(maxsize=1)
def load_geojson():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'Indian_States.json')
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Error: Indian_States.json file not found")
        return None
    except json.JSONDecodeError:
        st.error("Error: Invalid JSON file")
        return None

# Define constants
INDIA_LOCATION = [20.5937, 78.9629]
DEFAULT_ZOOM = 5

# Define mapping configurations
CROP_CONFIGS = {
    "Ragi": {
        "states": ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"],
        "colors": ('#752b2b', '#451a1a')
    },
    "Rice": {
        "states": ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"],
        "colors": ('#d6c3c3', '#736b6b')
    },
    "Wheat": {
        "states": ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"],
        "colors": ('#ba9e2f', '#d6660b')
    },
    "Sugarcane": {
        "states": ["Maharashtra", "Uttar Pradesh", "Karnataka", "Andhra Pradesh"],
        "colors": ('lightgreen', 'darkgreen')
    },
    "Maize": {
        "states": ["Madhya Pradesh", "Rajasthan", "Karnataka"],
        "colors": ('lightblue', 'darkblue')
    }
}

MOUNTAIN_CONFIGS = {
    "Himalayas": {
        "states": ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"],
        "colors": ('lightblue', 'blue')
    },
    "Western Ghats": {
        "states": ["Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu"],
        "colors": ('lightgreen', 'green')
    },
    "Eastern Ghats": {
        "states": ["Odisha", "Andhra Pradesh", "Tamil Nadu"],
        "colors": ('orange', 'darkorange')
    }
}

SOIL_CONFIGS = {
    "Alluvial": {
        "states": ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal"],
        "colors": ('lightyellow', 'gold')
    },
    "Red Soil": {
        "states": ["Chhattisgarh", "Orissa"],
        "colors": ('red', 'darkred')
    },
    "Arid": {
        "states": ["Gujarat", "Haryana"],
        "colors": ('#c2ac9b', 'brown')
    },
    "Clayey": {
        "states": ["Chhattisgarh", "Malwa"],
        "colors": ('darkgrey', 'grey')
    },
    "Peaty": {
        "states": ["Kerala", "West Bengal"],
        "colors": ('darkgreen', 'green')
    }
}

def create_india_map(highlight_states, highlight_color, highlight_border_color):
    folium_map = folium.Map(location=INDIA_LOCATION, zoom_start=DEFAULT_ZOOM)
    folium_map.add_child(folium.TileLayer("cartodb positron"))
    
    india_states = load_geojson()
    if not india_states:
        return folium_map

    def style_function(feature):
        state_name = feature['properties'].get('NAME_1')
        is_highlighted = state_name in highlight_states
        return {
            'fillColor': highlight_color if is_highlighted else 'transparent',
            'color': highlight_border_color if is_highlighted else 'black',
            'weight': 2,
            'dashArray': '5, 5' if is_highlighted else '0',
            'fillOpacity': 0.7
        }

    geojson_layer = folium.GeoJson(
        india_states,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['NAME_1'],
            aliases=['State:'],
            style="background-color: black; color: white; font-style: italic;"
        ),
        highlight_function=lambda x: {'weight': 3, 'color': 'blue', 'fillOpacity': 0.9}
    ).add_to(folium_map)

    folium_map.fit_bounds(geojson_layer.get_bounds())
    return folium_map

def main():
    st.sidebar.header("Options")
    main_option = st.sidebar.radio("Select one option", ["Crops", "Mountains", "Soil"])
    
    highlight_states = []
    highlight_color = 'yellow'
    highlight_border_color = 'red'

    if main_option == "Crops":
        with st.sidebar.expander("Crops Options"):
            crop_option = st.radio("Select a crop", list(CROP_CONFIGS.keys()))
            config = CROP_CONFIGS[crop_option]
            highlight_states = config["states"]
            highlight_color, highlight_border_color = config["colors"]
    
    elif main_option == "Mountains":
        with st.sidebar.expander("Mountain Options"):
            mountain_option = st.radio("Select a mountain range", list(MOUNTAIN_CONFIGS.keys()))
            config = MOUNTAIN_CONFIGS[mountain_option]
            highlight_states = config["states"]
            highlight_color, highlight_border_color = config["colors"]
    
    elif main_option == "Soil":
        with st.sidebar.expander("Soil Options"):
            soil_option = st.radio("Select a soil type", list(SOIL_CONFIGS.keys()))
            config = SOIL_CONFIGS[soil_option]
            highlight_states = config["states"]
            highlight_color, highlight_border_color = config["colors"]

    map = create_india_map(highlight_states, highlight_color, highlight_border_color)
    st_folium(map, width=725)

if __name__ == "__main__":
    main()