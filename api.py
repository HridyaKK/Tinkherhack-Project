from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load the GeoJSON data (Indian states)
with open(r'C:\Users\HP\Desktop\Tinkherhack\Indian_States.json') as f:
    india_states = json.load(f)

# Sample mappings for crops, mountains, and soil
crop_data = {
    "Ragi": ["Karnataka", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Uttarakhand"],
    "Rice": ["Kerala", "West Bengal", "Uttar Pradesh", "Punjab", "Tamil Nadu"],
    "Wheat": ["Punjab", "Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Uttarakhand"]
}

mountain_data = {
    "Himalayas": ["Jammu and Kashmir", "Himachal Pradesh", "Uttarakhand", "Sikkim", "Arunachal Pradesh"],
    "Western Ghats": ["Maharashtra", "Goa", "Karnataka", "Kerala", "Tamil Nadu"],
    "Eastern Ghats": ["Odisha", "Andhra Pradesh", "Tamil Nadu"]
}

soil_data = {
    "Alluvial": ["Punjab", "Haryana", "Uttar Pradesh", "Bihar", "West Bengal"],
    "Red Soil": ["Chhattisgarh", "Orissa"],
    "Arid": ["Gujarat", "Haryana"],
    "Clayey": ["Chhattisgarh", "Malwa"]
}

@app.route('/get_crops/<crop>', methods=['GET'])
def get_crops(crop):
    states = crop_data.get(crop, [])
    return jsonify(states)

@app.route('/get_mountains/<mountain>', methods=['GET'])
def get_mountains(mountain):
    states = mountain_data.get(mountain, [])
    return jsonify(states)

@app.route('/get_soil/<soil>', methods=['GET'])
def get_soil(soil):
    states = soil_data.get(soil, [])
    return jsonify(states)

#if __name__ == '__main__':
    #app.run(debug=True)
