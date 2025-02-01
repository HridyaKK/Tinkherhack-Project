import csv
import folium
import streamlit as st

# Function to create a CSV file with latitude, longitude, and additional information
def create_lat_long_csv(filename):
    data = [
        {"name": "Wheat Region", "latitude": 12.9716, "longitude": 77.5946, "crop": "Wheat", "soil": "Clay"},
        {"name": "Rice Region", "latitude": 28.7041, "longitude": 77.1025, "crop": "Rice", "soil": "Red"},
        {"name": "Mixed Region", "latitude": 19.0760, "longitude": 72.8777, "crop": "Rice", "soil": "Clay"},
        {"name": "Ragi Region", "latitude": 76.9598, "longitude": 15.3173, "crop": "Ragi", "soil": "Red"},
        {"name": "Maize Region", "latitude": 20.5937, "longitude": 78.9629, "crop": "Maize", "soil": "Sandy"},
        {"name": "Barley Region", "latitude": 25.5941, "longitude": 80.8248, "crop": "Barley", "soil": "Loamy"},
        {"name": "Cotton Region", "latitude": 19.1638, "longitude": 84.7956, "crop": "Cotton", "soil": "Clay"},
        # Added rivers
        {"name": "Ganges River", "latitude": 25.4358, "longitude": 82.0103, "crop": None, "soil": None},
        {"name": "Yamuna River", "latitude": 28.6139, "longitude": 77.2167, "crop": None, "soil": None},
        {"name": "Brahmaputra River", "latitude": 26.0383, "longitude": 90.5000, "crop": None, "soil": None},
        {"name": "Godavari River", "latitude": 17.9784, "longitude": 82.2387, "crop": None, "soil": None},
        {"name": "Narmada River", "latitude": 22.3039, "longitude": 74.3652, "crop": None, "soil": None}
    ]
    
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "latitude", "longitude", "crop", "soil"])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV file '{filename}' created successfully.")

# Create the CSV file
filename = "latitude_longitude.csv"
create_lat_long_csv(filename)

# Read the CSV file and extract latitude, longitude, crop, and soil data
locations = []
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        locations.append({
            "name": row["name"],
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"]),
            "crop": row["crop"],
            "soil": row["soil"]
        })

# Create a map centered at the first location
m = folium.Map(location=[locations[0]["latitude"], locations[0]["longitude"]], zoom_start=6)

# Define feature groups (layers) for crops, soils, and rivers
crops_layer = folium.FeatureGroup(name="Crops")
soils_layer = folium.FeatureGroup(name="Soils")
rivers_layer = folium.FeatureGroup(name="Rivers")

# Define layer colors for crops, soils, and rivers
crop_colors = {
    "Wheat": "green",
    "Rice": "blue",
    "Ragi": "purple",
    "Maize": "yellow",
    "Barley": "orange",
    "Cotton": "brown"
}

soil_colors = {
    "Clay": "yellow",
    "Red": "red",
    "Sandy": "gray",
    "Loamy": "green"
}

# Add markers for each location with crop, soil, or river information
for loc in locations:
    popup_content = f"Location: {loc['name']}"
    if loc["crop"]:  # Crop locations
        popup_content += f"<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}"
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=crop_colors.get(loc['crop'], 'gray'))
        ).add_to(crops_layer)
    elif loc["soil"]:  # Soil locations
        popup_content += f"<br>Soil: {loc['soil']}"
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=soil_colors.get(loc['soil'], 'gray'))
        ).add_to(soils_layer)
    elif loc["name"].endswith("River"):  # River locations
        folium.Marker(
            location=[loc["latitude"], loc["longitude"]],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color='blue', icon='cloud')  # River icon
        ).add_to(rivers_layer)

# Add the feature groups to the map
crops_layer.add_to(m)
soils_layer.add_to(m)
rivers_layer.add_to(m)

# Add layer control to toggle between different layers
folium.LayerControl().add_to(m)

# Streamlit checkbox to show/hide crops
show_wheat = st.checkbox('Show Wheat Regions', value=True)
show_rice = st.checkbox('Show Rice Regions', value=True)
show_ragi = st.checkbox('Show Ragi Regions', value=True)
show_maize = st.checkbox('Show Maize Regions', value=True)
show_barley = st.checkbox('Show Barley Regions', value=True)
show_cotton = st.checkbox('Show Cotton Regions', value=True)

# Filter the crops layer based on user input
if show_wheat:
    for loc in locations:
        if loc["crop"] == "Wheat":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Wheat", 'gray'))
            ).add_to(m)

if show_rice:
    for loc in locations:
        if loc["crop"] == "Rice":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Rice", 'gray'))
            ).add_to(m)

if show_ragi:
    for loc in locations:
        if loc["crop"] == "Ragi":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Ragi", 'gray'))
            ).add_to(m)

if show_maize:
    for loc in locations:
        if loc["crop"] == "Maize":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Maize", 'gray'))
            ).add_to(m)

if show_barley:
    for loc in locations:
        if loc["crop"] == "Barley":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Barley", 'gray'))
            ).add_to(m)

if show_cotton:
    for loc in locations:
        if loc["crop"] == "Cotton":
            folium.Marker(
                location=[loc["latitude"], loc["longitude"]],
                popup=folium.Popup(f"Location: {loc['name']}<br>Crop: {loc['crop']}<br>Soil: {loc['soil']}", max_width=300),
                icon=folium.Icon(color=crop_colors.get("Cotton", 'gray'))
            ).add_to(m)

# Save map as an HTML file
m.save("map.html")
print("Map has been created successfully!")

# Use Streamlit to display the map
st.components.v1.html(open("map.html", "r").read(), height=600)
