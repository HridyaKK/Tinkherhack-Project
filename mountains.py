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
st_folium(map, width=725)