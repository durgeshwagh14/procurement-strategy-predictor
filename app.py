import streamlit as st
import pickle
import numpy as np

# Load Model
with open("Process.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Kraljic Category Predictor", layout="centered")

st.title("📦 Procurement Strategy Predictor")
st.write("Predict Kraljic Category using ML Model")

st.markdown("---")

# User Inputs
lead_time = st.number_input("Lead Time (Days)", min_value=1, max_value=365, value=30)
order_volume = st.number_input("Order Volume (Units)", min_value=1, value=100)
cost_per_unit = st.number_input("Cost Per Unit", min_value=0.0, value=50.0)
supply_risk = st.slider("Supply Risk Score", 1, 10, 5)
profit_impact = st.slider("Profit Impact Score", 1, 10, 5)
environmental_impact = st.slider("Environmental Impact", 1, 10, 5)
single_source = st.selectbox("Single Source Risk", ["No", "Yes"])

# Convert Yes/No to 0/1
single_source = 1 if single_source == "Yes" else 0

# Prediction
if st.button("Predict Category"):
    
    input_data = np.array([[lead_time, order_volume, cost_per_unit,
                            supply_risk, profit_impact,
                            environmental_impact, single_source]])
    
    prediction = model.predict(input_data)[0]
    
    st.success(f"✅ Predicted Kraljic Category: {prediction}")


st.markdown("---")
