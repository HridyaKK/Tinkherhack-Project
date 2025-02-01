import csv
import folium

# Function to create a CSV file with latitude and longitude data
def create_lat_long_csv(filename):
    data = [
        {"name": "Region A", "latitude": 12.9716, "longitude": 77.5946},
        {"name": "Region B", "latitude": 28.7041, "longitude": 77.1025},
        {"name": "Region C", "latitude": 19.0760, "longitude": 72.8777},
    ]
    
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "latitude", "longitude"])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"CSV file '{filename}' created successfully.")

# Create the CSV file
filename = "latitude_longitude.csv"
create_lat_long_csv(filename)

# Read the CSV file and extract latitude and longitude data
locations = []
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        locations.append({
            "name": row["name"],
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"])
        })

# Create a map centered at the first location
m = folium.Map(location=[locations[0]["latitude"], locations[0]["longitude"]], zoom_start=6)

# Define layer colors
layer_colors = {
    "Crops": "green",
    "Mines": "gray",
    "Water Bodies": "blue",
    "Soil": "brown"
}

# Add markers for each location
for loc in locations:
    folium.Marker(
        location=[loc["latitude"], loc["longitude"]],
        popup=folium.Popup(f"Location: {loc['name']}", max_width=300)
    ).add_to(m)

folium.LayerControl().add_to(m)

# Save map as an HTML file
m.save("map.html")
print("Map has been created successfully!")
import streamlit as st

st.components.v1.html(open("map.html", "r").read(), height=600)

