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