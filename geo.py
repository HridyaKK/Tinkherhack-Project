import geopandas as gpd

# Load GeoJSON data (replace with your actual file paths)
geo_data_crops = gpd.read_file('crops_data.geojson')
geo_data_mines = gpd.read_file('mines_data.geojson')
