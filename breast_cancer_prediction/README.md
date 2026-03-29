# 🧬 Breast Cancer Prediction Web App

This project is a complete end-to-end Machine Learning application that predicts whether a breast tumor is **Malignant** or **Benign** based on clinical input data. It features a trained classification model integrated into a user-friendly Flask web interface.

## 📋 Table of Contents
* [Features](#-features)
* [Dataset](#-dataset)
* [Model & Analysis](#-model--analysis)
* [File Structure](#-file-structure)
* [How to Run](#-how-to-run)
* [Screenshots](#-screenshots)

---

## ✨ Features
* **Predictive Modeling:** Uses a trained Scikit-Learn model to classify tumors with high accuracy.
* **Web Interface:** Interactive UI built with Flask, HTML, and CSS for real-time predictions.
* **Data Scaling:** Includes a pre-configured scaler (`scaler.pkl`) to ensure input data is processed correctly.
* **Exploratory Data Analysis:** Comprehensive analysis included in Jupyter Notebooks.

## 📊 Dataset
The model is trained on the **Breast Cancer Wisconsin (Diagnostic) Dataset**. It includes features such as:
* Mean radius, texture, perimeter, and area.
* Smoothness, compactness, concavity, and symmetry.

## 🧠 Model & Analysis
* **Main Notebook:** `analysis-breast-cancer-prediction-dataset.ipynb` contains the full EDA, feature engineering, and model selection process.
* **Model:** The final trained model is saved as `breast_cancer_model.pkl`.
* **Scalability:** `scaler.pkl` is used to normalize user input before it reaches the model.

## 📂 File Structure
```text
breast_cancer_prediction/
├── static/              # CSS and images for the website
├── templates/           # HTML files (index.html, etc.)
├── app.py               # Flask application script
├── breast_cancer_model.pkl # Trained ML model
├── scaler.pkl           # Saved data scaler
├── breast_data.csv      # The raw dataset
└── main.ipynb           # Model development workflow
