import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🧠 ML Model Dashboard")
st.subheader("Interactive Prediction System")

st.write("Enter feature values to simulate prediction.")

# Sidebar Inputs
st.sidebar.header("Input Features")

feature1 = st.sidebar.slider("Feature 1", 0, 200, 100)
feature2 = st.sidebar.slider("Feature 2", 0.0, 1.0, 0.5)
feature3 = st.sidebar.slider("Feature 3", 0, 50, 25)

# Dummy Prediction Logic
def predict(f1, f2, f3):
    score = (f1 * 0.3) + (f2 * 50) + (f3 * 0.5)

    if score > 80:
        result = "High Risk"
        confidence = min(score, 100)
    else:
        result = "Low Risk"
        confidence = max(100 - score, 60)

    return result, round(confidence, 2)

# Prediction
if st.button("Predict"):

    result, confidence = predict(feature1, feature2, feature3)

    st.success(f"Prediction: {result}")
    st.info(f"Confidence Score: {confidence}%")

    # Visualization
    data = pd.DataFrame({
        "Features": ["Feature1", "Feature2", "Feature3"],
        "Values": [feature1, feature2, feature3]
    })

    st.subheader("Feature Visualization")

    fig, ax = plt.subplots()
    ax.bar(data["Features"], data["Values"])
    ax.set_title("Input Feature Values")

    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Built using Streamlit 🚀")
