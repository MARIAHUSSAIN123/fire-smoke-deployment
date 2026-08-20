🔥 Fire, Smoke & Normal Detection using CNN

📌 Project Overview

This project is an image classification system that detects whether an uploaded image represents Fire, Smoke, or a Normal scene.

The project uses Deep Learning with a baseline CNN and MobileNetV2 Transfer Learning. The trained model is integrated into a Streamlit application and exposed through a FastAPI REST API.

🎯 Objectives

Build an image classification model for Fire, Smoke and Normal scenes.

Train and evaluate a CNN-based model.

Apply MobileNetV2 Transfer Learning.

Build an interactive Streamlit application.

Expose the trained model through FastAPI.

Dockerize the application.

Prepare an automated CI/CD workflow.

🧠 Machine Learning Models

Baseline CNN

The baseline CNN achieved approximately 97.09% test accuracy.

MobileNetV2 Transfer Learning

MobileNetV2 was used with transfer learning for the three target classes.

The final model achieved approximately 97.40% test accuracy and was selected for the application.

🗂️ Classes

Class

Description

Fire

Image contains visible fire

Normal

Normal/non-fire scene

Smoke

Image contains smoke

📊 Model Evaluation

The model was evaluated on the test dataset using accuracy and additional evaluation methods.

The project includes:

Training and validation performance

Test-set evaluation

Confusion matrix

Classification report

Prediction results

Model

Test Accuracy

Baseline CNN

~97.09%

MobileNetV2

~97.40%

🚀 Streamlit Application

The Streamlit application allows users to upload an image and receive a Fire, Smoke, or Normal prediction.

Features

Image upload

Image preview

Three-class classification

Confidence percentage

MobileNetV2-based prediction

Interactive web interface

Run Streamlit

streamlit run app.py

⚡ FastAPI

A FastAPI backend exposes the trained model through REST endpoints.

GET /

Checks whether the API is running.

Example response:

{
  "message": "Fire Smoke Detection API is running"
}

GET /health

Checks API and model status.

Example response:

{
  "status": "healthy",
  "model": "loaded"
}

POST /predict

Accepts an image file and returns the predicted class, confidence, and probabilities.

Example response:

{
  "prediction": "Fire",
  "confidence": 97.42,
  "probabilities": {
    "Fire": 97.42,
    "Normal": 1.13,
    "Smoke": 1.45
  }
}

Run FastAPI

uvicorn main:app --reload

Swagger documentation:

http://127.0.0.1:8000/docs

Use POST /predict → Try it out → Upload image → Execute.

🐳 Docker

The project includes Docker support for packaging the application and its dependencies into a portable container.

Build

docker build -t fire-smoke-api .

Run

docker run -p 8000:8000 fire-smoke-api

Then open:

http://localhost:8000/docs

🔄 CI/CD

GitHub Actions is used to automate the development and deployment workflow.

Typical pipeline:

Developer
    ↓
Git Push
    ↓
GitHub Repository
    ↓
GitHub Actions
    ↓
Install Dependencies
    ↓
Build / Test
    ↓
Docker Build
    ↓
Docker Registry
    ↓
Deployment

The workflow can automatically build the Docker image and prepare it for deployment whenever changes are pushed to the configured branch.

📁 Project Structure

fire-detection-codex-api-main/
│
├── app.py
├── main.py
├── fire_smoke_detector.keras
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Fire Smoke Detection CNN.py
├── Fire Smoke Detector.py
└── README.md

🛠️ Technologies Used

Machine Learning

Python

TensorFlow

Keras

CNN

MobileNetV2

NumPy

Pillow

Application and API

Streamlit

FastAPI

Uvicorn

Python Multipart

DevOps

Docker

Git

GitHub

GitHub Actions

CI/CD

⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Enter the project directory:

cd fire-detection-codex-api-main

Install dependencies:

pip install -r requirements.txt

▶️ Running the Project

Streamlit

streamlit run app.py

FastAPI

uvicorn main:app --reload

Docker

docker build -t fire-smoke-api .
docker run -p 8000:8000 fire-smoke-api

🧪 API Testing

The API can be tested using:

FastAPI Swagger UI

Postman

Frontend applications

Swagger:

http://127.0.0.1:8000/docs

Upload a supported image through /predict to receive the classification result.

🖼️ Input Image Processing

Supported formats:

JPG

JPEG

PNG

Images are converted to RGB and resized to:

224 × 224 pixels

before inference.

📈 Results

The final MobileNetV2 model achieved approximately 97.40% test accuracy on the project's test dataset.

The system provides:

Image classification

Confidence scores

Streamlit interface

FastAPI REST API

Docker support

CI/CD-ready workflow

🔮 Future Improvements

Real-time CCTV/video detection

Live camera integration

Object detection with bounding boxes

Larger and more diverse datasets

Faster model inference

Cloud deployment

API authentication

Monitoring and logging

Automated model retraining

👩‍💻 Project Summary

This project demonstrates an end-to-end Deep Learning deployment workflow:

Dataset
   ↓
CNN / Transfer Learning
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Streamlit Application
   ↓
FastAPI REST API
   ↓
Docker
   ↓
CI/CD
   ↓
Deployment

It combines Deep Learning, Computer Vision, API Development, Docker and CI/CD practices into a complete image classification solution.

📄 License

This project is created for educational and project evaluation purposes.
