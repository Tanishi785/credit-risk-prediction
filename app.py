
import streamlit as st
import joblib
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="centered"
)

# Load trained model
model = joblib.load("credit_risk_model.pkl")

st.title("💳 Credit Risk Prediction")
st.write("Enter the customer's details to assess credit risk.")

st.divider()

st.subheader("👤 Customer Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

job = st.selectbox(
    "Job",
    [0, 1, 2, 3]
)

housing = st.selectbox(
    "Housing",
    ["own", "rent", "free"]
)

saving_accounts = st.selectbox(
    "Saving Accounts",
    ["little", "moderate", "quite rich", "rich"]
)

checking_account = st.selectbox(
    "Checking Account",
    ["little", "moderate", "rich"]
)

credit_amount = st.number_input(
    "Credit Amount",
    min_value=0,
    value=1000
)

duration = st.number_input(
    "Duration (months)",
    min_value=1,
    max_value=100,
    value=12
)

purpose = st.selectbox(
    "Purpose",
    [
        "car",
        "furniture/equipment",
        "radio/TV",
        "domestic appliances",
        "repairs",
        "education",
        "business",
        "vacation/others"
    ]
)

st.divider()

if st.button("🔍 Predict Credit Risk", use_container_width=True):

    # Create input data with exact model features
    input_data = pd.DataFrame([{
        "Age": age,
        "Job": job,
        "Credit amount": credit_amount,
        "Duration": duration,

        "Sex_male": 1 if sex == "male" else 0,

        "Housing_own": 1 if housing == "own" else 0,
        "Housing_rent": 1 if housing == "rent" else 0,

        "Saving accounts_moderate":
            1 if saving_accounts == "moderate" else 0,

        "Saving accounts_quite rich":
            1 if saving_accounts == "quite rich" else 0,

        "Saving accounts_rich":
            1 if saving_accounts == "rich" else 0,

        "Checking account_moderate":
            1 if checking_account == "moderate" else 0,

        "Checking account_rich":
            1 if checking_account == "rich" else 0,

        "Purpose_car":
            1 if purpose == "car" else 0,

        "Purpose_domestic appliances":
            1 if purpose == "domestic appliances" else 0,

        "Purpose_education":
            1 if purpose == "education" else 0,

        "Purpose_furniture/equipment":
            1 if purpose == "furniture/equipment" else 0,

        "Purpose_radio/TV":
            1 if purpose == "radio/TV" else 0,

        "Purpose_repairs":
            1 if purpose == "repairs" else 0,

        "Purpose_vacation/others":
            1 if purpose == "vacation/others" else 0
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.divider()
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.success("✅ Good Credit Risk")
        st.write("The customer is classified as having good credit risk.")
    else:
        st.error("⚠️ Bad Credit Risk")
        st.write("The customer is classified as having bad credit risk.")

st.caption("⚠️ This application is for educational/demo purposes.")