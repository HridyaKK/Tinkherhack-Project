import geopandas as gpd
import folium

map_center = {
  "type": "FeatureCollection",
  "generator": "overpass-turbo",
  "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
  "timestamp": "2025-02-02T02:47:13Z",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "@id": "relation/37973",
        "natural": "water",
        "type": "multipolygon",
        "water": "river"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              75.2239734,
              12.0238327
            ],
            [
              75.2240431,
              12.0236176
            ],
            [
              75.2239466,
              12.0229984
            ],
            [
              75.2238715,
              12.0226836
            ],
            [
              75.2238607,
              12.0223373
            ],
            [
              75.2236623,
              12.0221537
            ],
            [
              75.2235013,
              12.0219648
            ],
            [
              75.2237427,
              12.0218966
            ],
            [
              75.224027,
              12.0218546
            ],
            [
              75.2242792,
              12.021734
            ],
            [
              75.2244562,
              12.0215661
            ],
            [
              75.2245581,
              12.0214349
            ],
            [
              75.2248156,
              12.0212408
            ],
            [
              75.2250463,
              12.0209994
            ],
            [
              75.2252608,
              12.0206531
            ],
            [
              75.2253976,
              12.0203514
            ],
            [
              75.2256229,
              12.0205403
            ],
            [
              75.2259743,
              12.0206977
            ],
            [
              75.2264705,
              12.0208158
            ],
            [
              75.2271625,
              12.0208499
            ],
            [
              75.2279592,
              12.0208053
            ],
            [
              75.2282274,
              12.020821
            ],
            [
              75.2285278,
              12.0208761
            ],
            [
              75.2288443,
              12.0210257
            ],
            [
              75.2291266,
              12.0211401
            ],
            [
              75.2293405,
              12.0213285
            ],
            [
              75.228163,
              12.02165
            ],
            [
              75.2263606,
              12.022054
            ],
            [
              75.2258187,
              12.022096
            ],
            [
              75.225521,
              12.0222875
            ],
            [
              75.2252153,
              12.0223059
            ],
            [
              75.2250562,
              12.0223662
            ],
            [
              75.225065,
              12.0226784
            ],
            [
              75.22488,
              12.0229355
            ],
            [
              75.2246574,
              12.0234601
            ],
            [
              75.2245957,
              12.024541
            ],
            [
              75.2247566,
              12.0250079
            ],
            [
              75.2252743,
              12.0255352
            ],
            [
              75.2262915,
              12.0258594
            ],
            [
              75.227471,
              12.0260756
            ],
            [
              75.2277848,
              12.0260704
            ],
            [
              75.2290401,
              12.0264219
            ],
            [
              75.2300137,
              12.0268443
            ]
          ]
        ]
      }
    }
  ]
}  # Adjust the map center as per your data
m = folium.Map(location=map_center, zoom_start=12)

# Iterate through each feature and plot the river paths (using PolyLine)
for feature in gdf['geometry']:
    if feature.geom_type == 'Polygon':  # For regular polygons (single river path)
        coordinates = feature.exterior.coords  # Get the outer boundary coordinates
        folium.PolyLine(locations=coordinates, color="blue", weight=2.5, opacity=1).add_to(m)
    elif feature.geom_type == 'MultiPolygon':  # For multipolygon geometries (multiple river paths)
        for polygon in feature.geoms:
            coordinates = polygon.exterior.coords
            folium.PolyLine(locations=coordinates, color="blue", weight=2.5, opacity=1).add_to(m)

# Save the map as HTML to view in a browser
m.save("river_map.html")
