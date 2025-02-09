# Geoinfy 🎯


## Basic Details
### Team Name: Techrift


### Team Members
- Member 1: Arshiya Sulfikkar - Muthoot Institute of Technology and Science, Kochi
- Member 2: Hridya K K - Muthoot Institute of Technology and Science, Kochi
- Member 3: Jiya Joe Palathinkal - Muthoot Institute of Technology and Science, Kochi

### Hosted Project Link
https://geonify.streamlit.app/

### Project Description
This project helps school students explore an interactive map of India, showcasing various types of soils, crops, and mountains. By using Folium and Streamlit, the map allows students to learn about different agricultural regions, soil types, and mountain locations with interactive features, enabling them to select and view relevant information easily.


### The Problem statement
School students often struggle to access accurate and easily understandable information regarding the geographical distribution of soil types, crops, and mountains across India. Searching for this data across multiple websites can be time-consuming and inefficient.

### The Solution
This project provides an interactive map of India, enabling students to explore various soil types, crops, and mountains through an intuitive platform. By using Folium and Streamlit, the map allows students to visually interact with and learn about the geographical and agricultural features, enhancing their understanding in a user-friendly and engaging manner.


## Technical Details
### Technologies/Components Used
For Software:
- Languages : Python
- Frameworks : Streamlit
- Libraries
  - json (for JSON file handling)
  - os (for file/directory operations)
  - functools (for the lru_cache decorator)
  - folium (for creating interactive maps)
  - streamlit_folium (Streamlit component for Folium maps integration)
- Tools
  - VS Code (Code editor)
  - GitHub (Version control and repository hosting)
  - Git Bash (Command line interface for Git)
  - pip (Python package installer)

### Implementation
For Software:
# Installation
pip install streamlit
pip install folium
pip install streamlit-folium
python -m venv venv
venv\Scripts\activate

# Run
streamlit run main.py

### Project Documentation
For Software:

# Screenshots
![crops.jpg] 
*The states where the specified crop is cultivated are highlighted on the map.*

![Mountains.jpg]
*The states where the mountain ranges lie are highlighted on the map.*

![soil.jpg]
*The states where the specified type of soil is found are highlighted on the map.*

# User Flow
   1. The user starts the app by running the Streamlit command:  
      `streamlit run main.py`
   2. The app opens with the map centered on India.
   3. The user selects **Crops**, **Mountains**, or **Soil** from the sidebar.
   4. Based on the selection, the user chooses a specific crop, mountain range, or soil type.
   5. The map updates to highlight the relevant states with the chosen feature's colors.
   6. Users can interactively switch between categories and explore the map.

# Build Photos
![AHJ.jpg]

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*
