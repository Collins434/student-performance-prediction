import streamlit as st
import pandas as pd
import numpy as np

st.title("🎓 Student Performance Prediction System")

st.write("Enter the student details to predict the expected performance.")

# Input fields
hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.number_input("Previous Exam Score", 0, 100, 60)

st.subheader("Student Inputs")

data = {
    "Hours Studied": hours_studied,
    "Attendance": attendance,
    "Previous Score": previous_score
}

st.write(data)

# Prediction button
if st.button("Predict Performance"):

    # simple prediction formula (demo model)
    prediction = (hours_studied * 3) + (attendance * 0.3) + (previous_score * 0.5)

    st.success(f"Predicted Performance Score: {round(prediction,2)}")
