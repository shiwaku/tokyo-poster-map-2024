import json
import geojson

# Load the JSON file
with open('all.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Prepare the list of features for GeoJSON
features = []
for entry in data:
    point = geojson.Point((entry["long"], entry["lat"]))
    properties = {
        "area_id": entry["area_id"],
        "name": entry["name"],
        "status": entry["status"],
        "note": entry["note"],
        "long": entry["long"],
        "lat": entry["lat"],
    }
    features.append(geojson.Feature(geometry=point, properties=properties))

# Create a FeatureCollection
geojson_object = geojson.FeatureCollection(features)

# Output the GeoJSON object to a file
with open('all.geojson', 'w', encoding='utf-8') as f:
    geojson.dump(geojson_object, f)

print("GeoJSON conversion completed successfully!")
