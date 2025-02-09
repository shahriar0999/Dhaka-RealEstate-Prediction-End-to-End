import pytest
import sys
import os
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_management.fastapi_validation_model import HouseInfo
from main import app

client = TestClient(app)

valid_house_info = {
    'city_location': 5,
    'block_sector': 114,
    'bedroom': 3,
    'bathroom': 3,
    'sqrtFeet': 1340
 }

invalid_house_info = {
    "city_location": "Uttra",  # Invalid type (should be int/float)
    "block_sector": "Sector 12",  # Invalid type
    "bedroom": 2,
    "bathroom": 4,
    "sqrtFeet": 2015
}


def test_predict_house_price():
    """Test house price prediction with valid input"""
    response = client.post("/predict-house-price", json=valid_house_info)
    assert response.status_code == 200
    assert "Estimated House Price" in response.json()

def test_predict_house_price_invalid_data():
    """Test house price prediction with invalid input"""
    response = client.post("/predict-house-price", json=invalid_house_info)
    assert response.status_code == 422  # Unprocessable Entity (validation error)


def test_predict_rent_price():
    """Test rent price prediction with valid input"""
    response = client.post("/predict-rent-price", json=valid_house_info)
    assert response.status_code == 200
    assert "Estimated House Rent Amount" in response.json()


def test_predict_rent_price_invalid_data():
    """Test rent price prediction with invalid input"""
    response = client.post("/predict-rent-price", json=invalid_house_info)
    assert response.status_code == 422  # Unprocessable Entity (validation error)
