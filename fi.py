import json
import folium
import streamlit as st
from streamlit_folium import st_folium

# Define the base map function for India
def create_india_map(highlight_states=[], crop_images={}):
    # Coordinates for India (latitude and longitude)
    india_location = [20.5937, 78.9629]  # Centered on India
    # Create the base map centered on India with an initial zoom level
    folium_map = folium.Map(location=india_location, zoom_start=5)
    # Add zoom control and the default tile layer (can be customized)
    folium_map.add_child(folium.TileLayer("cartodb positron"))
   
    with open(r'C:\Users\HP\Desktop\Tinkherhack\Indian_States.json') as f:
        india_states = json.load(f)
    
    # Define markers for each selected crop and state
    state_coords = {
        "Karnataka": [15.3173, 75.7139],
        "Andhra Pradesh": [15.9129, 79.7400],
        "Tamil Nadu": [11.1271, 78.6569],
        "Maharashtra": [19.6632, 75.3202],
        "Uttarakhand": [30.0668, 79.0193],
        "Kerala": [10.8505, 76.2711],
        "West Bengal": [22.9868, 87.8550],
        "Uttar Pradesh": [27.1595, 79.4105],
        "Punjab": [31.1471, 75.3412],
        "Odisha": [20.9517, 85.0985],
        "Rajasthan": [27.0238, 74.2179],
        "Goa": [15.2993, 74.1240],
        "Himachal Pradesh": [32.0787, 77.1734],
        "Jammu and Kashmir": [33.7787, 76.5762],
        "Sikkim": [27.5330, 88.6130],
        "Arunachal Pradesh": [27.1026, 93.6053]
    }

    # Add markers to the map with images for selected crops
    for state in highlight_states:
        if state in state_coords:
            # Add marker for each state in the highlight states
            coords = state_coords[state]
            image_url = crop_images.get(state, None)  # Get the corresponding image URL for the state
            
            if image_url:  # If an image URL is found
                folium.Marker(
                    location=coords,
                    popup=folium.Popup(f'<img src="{image_url}" width="200px" height="200px">', max_width=300),
                    icon=folium.Icon(color="blue")
                ).add_to(folium_map)
    
    # Fit the map to the bounds of the GeoJSON layer
    folium_map.fit_bounds([state_coords[state] for state in highlight_states if state in state_coords])
    return folium_map

# Add the main radio button for selecting options
st.sidebar.header("Options")
main_option = st.sidebar.radio("Select one option", ["Crops", "Mountains", "Soil"])

# Logic based on the selected main option
highlight_states = []
highlight_color = 'yellow'
highlight_border_color = 'red'

crop_images = {
    "Ragi": "https://www.atulyam.co.in/cdn/shop/articles/ragi_picture.jpg?v=1705326736&width=1100",  # Replace with actual image URL for Ragi
    "Rice": "https://m.media-amazon.com/images/I/81Voy6TeZtL.jpg",  # Replace with actual image URL for Rice
    "Wheat": "https://www.healthyorganic.in/cdn/shop/products/red_fife__85088_9b450a69-7054-47c0-8645-558498a9b7c5_2048x.jpg?v=1563382574",  # Replace with actual image URL for Wheat
    "Sugarcane": "https://cdn.prod.website-files.com/6447cf709b168c44f3d5bb50/65f83b457a3ffa9b38415a1e_Ontwerp%20zonder%20titel%20-%202024-03-18T140151.702.webp",  # Replace with actual image URL for Sugarcane
    "Maize": "https://cdn.wikifarmer.com/images/thumbnail/2022/04/maize-nutritional-value-1200x630.jpg"  # Replace with actual image URL for Maize
}

if main_option == "Crops":
    show_crops = True
    with st.sidebar.expander("Crops Options"):
        crop_option = st.radio("Select a crop", ["Rice", "Wheat", "Ragi", "Sugarcane", "Maize"])
        if crop_option == "Ragi":
            highlight_states = ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"]
        elif crop_option == "Rice":
            highlight_states = ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"]
        elif crop_option == "Wheat":
            highlight_states = ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
        elif crop_option == "Sugarcane":
            highlight_states = ["Maharashtra", "Uttar Pradesh", "Karnataka", "Andhra Pradesh"]
        elif crop_option == "Maize":
            highlight_states = ["Madhya Pradesh", "Rajasthan", "Karnataka"]

elif main_option == "Mountains":
    show_mountains = True
    with st.sidebar.expander("Mountain Options"):
        mountain_option = st.radio("Select a mountain range", ["Himalayas", "Western Ghats", "Eastern Ghats"])
        if mountain_option == "Himalayas":
            highlight_states = ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"]
        elif mountain_option == "Western Ghats":
            highlight_states = ["Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu"]
        elif mountain_option == "Eastern Ghats":
            highlight_states = ["Odisha", "Andhra Pradesh", "Tamil Nadu"]

elif main_option == "Soil":
    show_soil = True
    with st.sidebar.expander("Soil Options"):
        soil_option = st.radio("Select a soil type", ["Alluvial", "Red Soil", "Arid", "Clayey", "Peaty"])
        if soil_option == "Alluvial":
            highlight_states = ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal"]
        elif soil_option == "Red Soil":
            highlight_states = ["Chhattisgarh", "Orissa"]
        elif soil_option == "Arid":
            highlight_states = ["Gujarat", "Haryana"]
        elif soil_option == "Clayey":
            highlight_states = ["Chhattisgarh", "Malwa"]
        elif soil_option == "Peaty":
            highlight_states = ["Kerala", "West Bengal"]

# Create the map for India with the selected options
map = create_india_map(highlight_states=highlight_states, crop_images=crop_images)

# Render the map in Streamlit
st_folium(map, width=725)
