import streamlit as st

st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="centered"
)

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

if st.button("🔮 Predict Credit Risk", use_container_width=True):
    st.info("Prediction will be connected to the trained ML model.")