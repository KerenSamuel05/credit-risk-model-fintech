# 💳 Credit Risk Prediction App

A machine learning-powered web application that predicts the probability of loan default based on applicant financial and demographic data. Built using Python, Scikit-learn, and Streamlit, and deployed as an interactive web app.

---

## 🚀 Live Demo

👉 *https://credit-risk-model-fintech-5xiauoafjveggybkge37v8.streamlit.app*

---

## 🧠 Project Overview

This project aims to simulate a real-world credit risk assessment system used in financial institutions. Users can input applicant details such as income, loan amount, credit history, and more, and receive an instant prediction of default risk along with a probability score.

The model is designed to prioritize identifying high-risk applicants, reflecting real-world lending scenarios where minimizing default risk is critical.

---

## ⚙️ Features

* Interactive web UI using Streamlit
* Real-time credit risk prediction
* Probability-based risk scoring
* Handles categorical data using one-hot encoding
* Includes data preprocessing (missing values, scaling, feature engineering)
* Clean and user-friendly interface

---

## 🏗️ Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit

---

## 📊 Machine Learning Model

* Model: Logistic Regression
* Class imbalance handled using `class_weight='balanced'`
* Feature scaling applied using StandardScaler
* Evaluation metrics considered:

  * Accuracy
  * Precision & Recall
  * Classification Report

The model is tuned to **prioritize recall for high-risk cases**, ensuring risky applicants are less likely to be misclassified as safe.

---

## 📁 Project Structure

```
credit-risk-app/
│
├── app.py              # Streamlit application
├── model.pkl           # Trained ML model
├── scaler.pkl          # Scaler used during training
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## 🧪 Input Features

The model uses 22 features including:

* Personal Information:

  * Age
  * Income
  * Employment Length
  * Credit History Length

* Loan Details:

  * Loan Amount
  * Interest Rate
  * Loan-to-Income Ratio

* Categorical Variables:

  * Home Ownership
  * Loan Intent
  * Loan Grade
  * Default History

Categorical features are encoded using one-hot encoding to match training data.

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 🌍 Deployment

The app is deployed using Streamlit Community Cloud for easy access and sharing.

---

## 💡 Future Improvements

* Add model comparison (Logistic Regression vs Decision Tree)
* Improve UI design with better visualizations
* Add feature importance explanation
* Integrate real datasets or APIs
* Enhance validation and user feedback

---

## 📌 Key Takeaways

* Built an end-to-end ML pipeline from preprocessing to deployment
* Handled real-world challenges like class imbalance and feature engineering
* Developed a user-facing ML application, not just a model

---

## 🤝 Connect

If you found this project interesting or have feedback, feel free to connect!

---

