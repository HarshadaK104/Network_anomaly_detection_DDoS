# 🛡️ DDoS Detection Using Machine Learning

A real-time network traffic anomaly detection system leveraging unsupervised machine learning models to identify potential Distributed Denial of Service (DDoS) attacks. Built with a Flask backend and React frontend, this project demonstrates practical deployment of ML for cybersecurity.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Model](#model)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Testing](#testing)
- [Future Work](#future-work)
- [License](#license)

---

## 📖 Overview

With the growing frequency and sophistication of cyber threats, traditional rule-based intrusion detection systems fall short. This project presents a lightweight, real-time system to detect DDoS traffic using unsupervised ML models like Isolation Forest and One-Class SVM. The system is trained on the CICIDS dataset and features:

- Binary classification of network traffic (Benign vs DDoS)
- Real-time file upload and prediction
- Visualization via a modern web interface

---

## 🧰 Tech Stack

### Machine Learning
- `TensorFlow`, `Keras` – for model creation and training
- `Scikit-learn` – preprocessing, evaluation, and model utilities

### Python Ecosystem
- `Pandas`, `NumPy` – data manipulation

### Backend
- `Flask` – lightweight API server for model prediction

### Frontend
- `HTML`, `CSS` – simple UI for uploading CSV files and viewing results
- (Optional extension: `React` dashboard)

### Tools
- `Jupyter Notebook`, `VS Code`, `Terminal`
- `pip` for managing dependencies

---

## 📊 Dataset

The project uses the **CICIDS 2018 Dataset**, which includes both benign and DDoS attack traffic samples. Features such as IP address, packet size, duration, and protocol are extracted and used for training the model.

- 📁 Format: CSV
- ⚙️ Preprocessing: Feature scaling, label encoding, and filtering

---

## 🧠 Model

Unsupervised learning models were chosen for their ability to detect unknown attack patterns:
- **Isolation Forest** – Tree-based anomaly detection
- **One-Class SVM** – High recall, ideal for identifying rare attack behaviors

Evaluation Metrics:
- Accuracy: up to **98.1%**
- False Alarm Rate: as low as **0.8%**
- F1-Score: up to **98.3%**

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ddos-ml-detector.git
   cd ddos-ml-detector

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the Flask server**
   ```bash
   python app.py
   
4.**Access Frontend**
Open index.html in your browser and upload a CSV file to test.

---
## 🔍 How It Works

1) User uploads a network traffic CSV file via the UI.
2) The file is sent to the Flask backend.
3) The trained ML model analyzes the traffic and classifies flows as benign or DDoS.
4) The result is returned and displayed in the UI.
