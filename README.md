# 🌊 AquaGuard - AI Water Quality Monitoring System

**Capstone Project | Artificial Intelligence**  
**SDG 6: Clean Water and Sanitation**

---

## 📋 Project Overview

AquaGuard is an AI-powered web application that helps users check if water is safe to drink by analyzing key water quality parameters. It aims to reduce waterborne diseases by providing instant, accessible water safety predictions.

### 🎯 Problem Statement
Many areas in Mumbai and India lack quick and affordable water quality testing. Contaminated water causes serious health issues. Traditional testing is slow and expensive.

### ✅ Solution
An interactive web app built with **Streamlit** and **Machine Learning** (Random Forest Classifier) that predicts water potability in real-time.

---

## ✨ Key Features

- **Real-time Water Quality Prediction** using 9 important parameters (pH, Turbidity, Hardness, etc.)
- **Confidence Score** for each prediction
- **Image Upload Interface** (ready for future CNN model)
- **Interactive Dashboard** with visualizations
- **User-friendly Interface**

---

## 🛠 Technology Stack

- **Language**: Python
- **ML Library**: Scikit-learn (Random Forest)
- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Others**: Pandas, NumPy, Joblib

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd AquaGuard

2. Install requirements
    ```bash
   pip install -r requirements.txt

3. Train model
    ```bash
    python train_model.py

4. Run application
    ```bash
    streamlit run app.py

## Porject Structure
    ```bash
    AquaGuard/
    ├── app.py                    # Main Streamlit Application
    ├── train_model.py            # Model Training Script
    ├── water_model.pkl           # Trained Model
    ├── water_potability.csv      # Dataset
    ├── requirements.txt
    ├── README.md
    ├── screenshots/              # Screenshots folder
    └── report.pdf                # Project Documentation

## Dataset
Used <a href="https://www.kaggle.com/datasets/adityakadiwal/water-potability" target="_blank">Water Potability Dataset</a> from Kaggle.

## 🔮 Future Scope
- Integration of CNN for direct image-based analysis
- Mobile Application (Flutter)
- IoT sensor integration
- Real-time alerts via SMS/Email
- Deployment on cloud (AWS/Heroku)

<a href="https://www.example.com" target="_blank">Open in New Tab</a>
