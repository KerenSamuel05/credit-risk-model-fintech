# 🏦 Credit Risk Prediction Model

A machine learning project focused on predicting **loan default risk** using borrower financial and behavioral data. This project simulates how financial institutions assess creditworthiness and balance **risk vs business growth**.

---

## 🚀 Project Overview

The goal of this project is to build and evaluate models that can predict whether a borrower is likely to default on a loan.

Instead of focusing purely on code, this project follows a **problem-first, iterative development approach**, leveraging AI-assisted workflows to rapidly prototype, test, and refine models while maintaining a strong focus on **financial reasoning and model interpretation**.

---

## 📊 Dataset Features

The dataset includes borrower-level information such as:

- Age, Income, Employment Length  
- Loan Amount, Interest Rate  
- Loan Intent & Grade  
- Home Ownership Status  
- Historical Default Indicator  

**Target Variable:**
- `loan_status` → 0 (No Default), 1 (Default)

---

## ⚙️ Workflow

### 1. Data Preprocessing
- Handled missing values using median imputation  
- Removed unrealistic values (e.g., extreme age/employment length)  
- Encoded categorical variables using one-hot encoding  

### 2. Feature Engineering
- Focused on financially relevant indicators such as:
  - Loan-to-income ratio  
  - Interest rate  
  - Credit history  

### 3. Model Building

#### 🔹 Logistic Regression
- Baseline model for binary classification  
- Applied **StandardScaler** for feature normalization  
- Improved using `class_weight='balanced'` to address class imbalance  

#### 🔹 Decision Tree Classifier
- Captures non-linear relationships  
- Used for comparison against Logistic Regression  

---

## 📈 Model Performance

### Logistic Regression (Balanced)
- Accuracy: ~80%  
- Recall (Default): **78%**  
- Strong at identifying high-risk borrowers  

### Decision Tree
- Accuracy: ~90%  
- Recall (Default): **58%**  
- Better overall accuracy but weaker in risk detection  

---

## ⚖️ Key Insight

> In credit risk modeling, **recall is more important than accuracy**.

- Logistic Regression performed better in detecting defaulters  
- Decision Tree performed better in overall classification accuracy  

This highlights the trade-off between:
- **Risk Control (minimizing defaults)**  
- **Business Growth (approving more customers)**  

---

## 🎯 Threshold Tuning

Instead of relying on a fixed 0.5 threshold, probability-based predictions were used:

- Lower threshold → Higher recall (more risk detection)  
- Higher threshold → Fewer false positives (more approvals)  

This mirrors real-world lending strategies where models are tuned based on business objectives.

---

## 💼 Business Impact

This model demonstrates how financial institutions:

- Assess borrower risk using data  
- Optimize approval strategies  
- Balance profitability with default risk  

---

## 🧠 Key Learnings

- Model evaluation must go beyond accuracy  
- Recall is critical in risk-sensitive domains  
- Feature scaling improves model convergence  
- AI-assisted workflows can accelerate development while maintaining analytical depth  

---

## 🛠️ Tech Stack

- Python  
- pandas  
- scikit-learn  
- matplotlib (for visualization)  
- Google Colab  

---

## 📌 Future Improvements

- Implement Random Forest / Gradient Boosting  
- Hyperparameter tuning  
- ROC-AUC analysis  
- Deployment as a simple web app  

---

## 🤝 Contributing

Open to suggestions, improvements, and discussions!

---

## 📬 Connect

If you're interested in fintech, data analytics, or machine learning, feel free to connect or reach out!
