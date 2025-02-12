import streamlit as st
import requests
import json

# Define the API endpoint
API_URL = "http://54.211.99.121:8501/"
headers = {
  'Content-Type': 'application/json'
}

# Load JSON data for HouseDF
with open('city_area_dict_houseDf.json', 'r') as f1:
    area_housedf = json.load(f1)

with open('block_sector_dict_houseDf.json', 'r') as f:
    block_housedf = json.load(f)  


# for RentDF
with open('city_area_dict_rentDf.json', 'r') as f1:
    area_rentdf = json.load(f1)

with open('block_sector_dict_rentDf.json', 'r') as f:
    block_rentdf = json.load(f)  



# Extract keys from the JSON dictionary for HouseDF
area_housedf_list = list(area_housedf.keys())
block_housedf_list = list(block_housedf.keys())

# RentDF
area_rentdf_list = list(area_rentdf.keys())
block_rentdf_list = list(block_rentdf.keys())



# Title
st.title('End-to-End House Price and Rent Prediction Dhaka City')

# Dropdown to select the model
model = st.selectbox("Select Model", ["House Rent Prediction", "House Price Prediction"])

# Display dropdown for block/area based on the selected model
if model == "House Price Prediction":
    city_location = st.selectbox("Select City Location", area_housedf_list)
    block_sector = st.selectbox("Select Block/Area of your Location", block_housedf_list)
    bedroom = st.selectbox("Number of BedRoom", [1, 2, 3, 4, 5])
    bathroom = st.selectbox("Number of BathRoom", [1, 2, 3, 4])
    sqrtFeet = st.slider("SquareFeet of Flat/Appartment", 300, 3000, 1200, 10)

    data = {"city_location": area_housedf[city_location],
    "block_sector": block_housedf[block_sector],
    "bedroom": bedroom,
    "bathroom": bathroom,
    "sqrtFeet": sqrtFeet}
    
    model_api = "predict-house-price"

elif model == "House Rent Prediction":
    city_location = st.selectbox("Select City Location", area_rentdf_list)
    block_sector = st.selectbox("Select Block/Area of your Location", block_rentdf_list)
    bedroom = st.selectbox("Number of BedRoom", [1, 2, 3, 4, 5])
    bathroom = st.selectbox("Number of BathRoom", [1, 2, 3, 4])
    sqrtFeet = st.slider("SquareFeet of Flat/Appartment", 300, 3000, 1200, 10)
    
    data = {"city_location": area_rentdf[city_location],
    "block_sector": block_rentdf[block_sector],
    "bedroom": bedroom,
    "bathroom": bathroom,
    "sqrtFeet": sqrtFeet}

    model_api = "predict-rent-price"

if st.button("Predict"):
    with st.spinner("Predicting.... Please Wait!!!!!!!!!"):
        response = requests.post(API_URL+model_api, json=data, headers=headers)

        output = response.json()

    st.write(output)