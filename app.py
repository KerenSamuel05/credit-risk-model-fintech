import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model + scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Credit Risk App", layout="centered")

st.title("💳 Credit Risk Predictor")
st.write("Assess the risk level of a loan applicant using ML")

# ----------- PERSONAL INFO -----------
st.subheader("👤 Personal Information")

age = st.number_input("Age", min_value=18, max_value=80)
income = st.number_input("Annual Income")
emp_length = st.number_input("Employment Length (years)", min_value=0, max_value=40)
cred_hist = st.number_input("Credit History Length")

# ----------- LOAN DETAILS -----------
st.subheader("💰 Loan Details")

loan_amnt = st.number_input("Loan Amount")
interest_rate = st.number_input("Interest Rate (%)")
loan_percent_income = st.number_input("Loan % of Income")

# ----------- CATEGORICAL INPUTS -----------
st.subheader("📊 Additional Details")

home = st.selectbox("Home Ownership", ["OWN", "RENT", "OTHER"])
intent = st.selectbox("Loan Intent", ["EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"])
grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
default = st.selectbox("Previous Default", ["No", "Yes"])

# ----------- PREDICTION -----------

if st.button("Predict Risk"):

    # Basic validation
    if income <= 0:
        st.warning("Income must be greater than 0")
    else:
        try:
            # Base dictionary
            input_dict = {
                'person_age': age,
                'person_income': income,
                'person_emp_length': emp_length,
                'loan_amnt': loan_amnt,
                'loan_int_rate': interest_rate,
                'loan_percent_income': loan_percent_income,
                'cb_person_cred_hist_length': cred_hist,

                # Default dummy values
                'person_home_ownership_OTHER': 0,
                'person_home_ownership_OWN': 0,
                'person_home_ownership_RENT': 0,

                'loan_intent_EDUCATION': 0,
                'loan_intent_HOMEIMPROVEMENT': 0,
                'loan_intent_MEDICAL': 0,
                'loan_intent_PERSONAL': 0,
                'loan_intent_VENTURE': 0,

                'loan_grade_B': 0,
                'loan_grade_C': 0,
                'loan_grade_D': 0,
                'loan_grade_E': 0,
                'loan_grade_F': 0,
                'loan_grade_G': 0,

                'cb_person_default_on_file_Y': 0
            }

            # Set categorical values
            input_dict[f'person_home_ownership_{home}'] = 1
            input_dict[f'loan_intent_{intent}'] = 1

            if grade != "A":
                input_dict[f'loan_grade_{grade}'] = 1

            if default == "Yes":
                input_dict['cb_person_default_on_file_Y'] = 1

            # Convert to DataFrame
            input_df = pd.DataFrame([input_dict])

            # Ensure correct column order
            columns_order = ['person_age', 'person_income', 'person_emp_length', 'loan_amnt', 'loan_int_rate',
                             'loan_percent_income', 'cb_person_cred_hist_length',
                             'person_home_ownership_OTHER', 'person_home_ownership_OWN', 'person_home_ownership_RENT',
                             'loan_intent_EDUCATION', 'loan_intent_HOMEIMPROVEMENT', 'loan_intent_MEDICAL',
                             'loan_intent_PERSONAL', 'loan_intent_VENTURE',
                             'loan_grade_B', 'loan_grade_C', 'loan_grade_D', 'loan_grade_E',
                             'loan_grade_F', 'loan_grade_G',
                             'cb_person_default_on_file_Y']

            input_df = input_df[columns_order]

            # Scale input
            input_scaled = scaler.transform(input_df)

            # Predict
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0][1]

            # ----------- OUTPUT -----------

            st.subheader("📈 Prediction Result")

            if prediction == 1:
                st.error(f"⚠️ High Risk Applicant")
            else:
                st.success(f"✅ Low Risk Applicant")

            # Probability bar
            st.progress(int(probability * 100))
            st.write(f"**Risk Probability:** {probability:.2%}")

            # Insight
            st.markdown("### 🧠 Model Insight")
            st.write("This model prioritizes identifying high-risk applicants to reduce default risk.")

        except Exception as e:
            st.error(f"Error: {e}")