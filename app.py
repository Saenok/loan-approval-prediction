
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("loan_model.pkl")

st.title("Loan Approval Prediction")

loan_id = st.number_input("Loan ID", min_value=1)
no_of_dependents = st.number_input("Number of Dependents", min_value=0)
education = st.selectbox("Education", [0, 1])
self_employed = st.selectbox("Self Employed", [0, 1])

income_annum = st.number_input("Annual Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
cibil_score = st.number_input("CIBIL Score")

residential_assets_value = st.number_input("Residential Assets Value")
commercial_assets_value = st.number_input("Commercial Assets Value")
luxury_assets_value = st.number_input("Luxury Assets Value")
bank_asset_value = st.number_input("Bank Asset Value")

if st.button("Predict"):

    data = np.array([[loan_id,
                      no_of_dependents,
                      education,
                      self_employed,
                      income_annum,
                      loan_amount,
                      loan_term,
                      cibil_score,
                      residential_assets_value,
                      commercial_assets_value,
                      luxury_assets_value,
                      bank_asset_value]])

    prediction = model.predict(data)

    if prediction[0] == 0:
    st.success("Loan Approved")
else:
    st.error("Loan Rejected")
    
