# House Price and Rent Prediction of Dhaka 

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.4%2B-orange)
![Docker](https://img.shields.io/badge/Docker-24.00%2B-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-2.4970-red)

This project is an **end-to-end machine learning pipeline** for predicting **house prices** and **rent prices** in Dhaka, Bangladesh. It includes a FastAPI backend for serving predictions, a Streamlit frontend for user interaction, and a CI/CD pipeline using Jenkins for deployment to AWS EC2.

---


## Table of Contents
- [House Price and Rent Prediction of Dhaka](#house-price-and-rent-prediction-of-dhaka)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Installation](#installation)
      - [Example response:](#example-response)
  - [Deployment](#deployment)
    - [1. **Local Deployment**](#1-local-deployment)
    - [2. **AWS EC2 Deployment**](#2-aws-ec2-deployment)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

---

## Project Overview
The project aims to provide nearly accurate predictions for house prices and rent prices in Dhaka based on features such as:
- Location Area
- Size (square footage)
- Number of bedrooms and bathrooms


The system is built using:
- **FastAPI** for the backend API
- **Streamlit** for the frontend interface
- **Docker** for containerization
- **Jenkins** for CI/CD deployment to AWS EC2

---

---

## Features
- **House Price Prediction**: Predict the price of a house based on its features.
- **Rent Price Prediction**: Predict the monthly rent of a property based on its features.
- **FastAPI Backend**: REST API for serving predictions.
- **Streamlit Frontend**: User-friendly interface for interacting with the API.
- **Dockerized**: Containerized for easy deployment.
- **CI/CD Pipeline**: Automated deployment using Jenkins.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shahriar0999/Dhaka-RealEstate-Prediction-End-to-End.git

   cd Dhaka-RealEstate-Prediction-End-to-End
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build

## Usage

### 1. **FastAPI Backend**
- The FastAPI backend serves predictions via REST API.
- Access the API at `http://localhost:8501`.
- Use the `/predict-rent-price`  and `/predict-house-price` endpoint to get predictions.

#### Example Request:
```json
POST /predict-house-price
{
  "city_location": "Gulshan",
  "block_sector": "Gulshan 1",
  "bedrooms": 2,
  "bathrooms": 2,
  "sqrtFeet": 1200,
}
```

#### Example response:
```json
{
  "Estimated House Rent Price": 25000000৳
}
```

## Deployment

### 1. **Local Deployment**
To run the application locally using Docker:
1. Build and start the containers:
   ```bash
   docker-compose up --build

### 2. **AWS EC2 Deployment**
To deploy the application to AWS EC2 using Jenkins:
1. **Set Up Jenkins**:
   - Ensure Jenkins is installed and configured with AWS credentials.
   - Install necessary plugins (e.g., Docker, AWS CLI).

2. **Configure Jenkins Pipeline**:
   - Use the `Jenkinsfile` provided in the repository.
   - The pipeline will:
     - Build Docker images for FastAPI and Streamlit.
     - Run unit and integration tests.
     - Deploy the application to an EC2 instance.

3. **Deploy to EC2**:
   - Start the Jenkins pipeline.
   - Once deployed, access the application using the EC2 instance's public IP:
     - FastAPI: `http://<EC2_PUBLIC_IP>:8501`
     - Streamlit: `http://<EC2_PUBLIC_IP>:8502`

4. **Post-Deployment**:
   - Monitor the application using AWS CloudWatch.
   - Set up auto-scaling and load balancing if needed.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


## Acknowledgments

- **Open-Source Community**: Thanks to the open-source community for providing valuable tools and libraries.
