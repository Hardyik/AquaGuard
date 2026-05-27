import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import plotly.express as px
import sklearn

st.set_page_config(page_title="AquaGuard", layout="wide")
st.title("🌊 AquaGuard - AI Water Quality Monitoring")
st.markdown("**SDG 6: Clean Water and Sanitation**")

# Load model
model = joblib.load('water_model.pkl')

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict with Parameters", "Image Analysis (Demo)", "Dashboard"])

if page == "Home":
   st.write("""
    ### Welcome to AquaGuard
    An AI solution to detect unsafe drinking water and prevent waterborne diseases.
    """) 
   st.image("https://images.unsplash.com/photo-1527066236128-2ff79f7b9705?q=80&w=1176&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="Clean Water")

elif page == "Predict with Parameters":
    st.header("🔬 Water Quality Prediction using Parameters")
    
    col1, col2 = st.columns(2)
    with col1:
        ph = st.slider("pH Level", 0.0, 14.0, 7.0)
        hardness = st.slider("Hardness (mg/L)", 0.0, 500.0, 150.0)
        solids = st.slider("Solids (ppm)", 0.0, 50000.0, 20000.0)
    
    with col2:
        turbidity = st.slider("Turbidity (NTU)", 0.0, 10.0, 2.5)
        chloramines = st.slider("Chloramines (ppm)", 0.0, 10.0, 3.0)
        sulfate = st.slider("Sulfate (mg/L)", 0.0, 500.0, 250.0)
    
    if st.button("🔍 Check Water Safety", type="primary"):
        input_data = pd.DataFrame([{
            'ph': ph, 'Hardness': hardness, 'Solids': solids,
            'Chloramines': chloramines, 'Sulfate': sulfate,
            'Conductivity': 400, 'Organic_carbon': 10,
            'Trihalomethanes': 70, 'Turbidity': turbidity
        }])
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        if prediction == 1:
            st.success(f"✅ **SAFE TO DRINK** (Confidence: {probability*100:.1f}%)")
        else:
            st.error(f"❌ **UNSAFE** (Confidence: {(1-probability)*100:.1f}%)")

elif page == "Image Analysis (Demo)":
    st.header("📸 Water Image Analysis")
    st.info("Note: This is a demo version. Advanced CNN model can be added later.")
    
    uploaded_file = st.file_uploader("Upload water sample photo", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.warning("🔬 In real version, CNN model would analyze color, turbidity, and contamination.")

elif page == "Dashboard":
    st.header("📊 Water Quality Dashboard")
    st.write("Sample visualization (you can expand this)")
    data = pd.DataFrame({
        'Parameter': ['pH', 'Turbidity', 'Hardness'],
        'Value': [7.2, 1.8, 145]
    })
    fig = px.bar(data, x='Parameter', y='Value')
    st.plotly_chart(fig)

st.caption("AquaGuard - AI for SDG 6 | Capstone Project")
