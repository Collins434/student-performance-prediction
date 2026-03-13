
import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict whether the student will PASS or FAIL.")

model = joblib.load("student_model.pkl")

study_hours = st.slider("Study Hours per Week", 0, 40, 10)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.slider("Previous Score", 0, 100, 60)
assignments = st.slider("Assignments Completed", 0, 10, 5)
participation = st.slider("Participation Level (1-10)", 1, 10, 5)

internet_access = st.selectbox("Internet Access", ["Yes", "No"])
study_environment = st.selectbox("Study Environment", ["Poor", "Average", "Good"])

internet_access = 1 if internet_access == "Yes" else 0
env_map = {"Poor":0, "Average":1, "Good":2}
study_environment = env_map[study_environment]

if st.button("Predict Result"):
    features = np.array([[study_hours,
                          attendance,
                          previous_score,
                          assignments,
                          participation,
                          internet_access,
                          study_environment]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ The student is likely to PASS")
    else:
        st.error("⚠️ The student is likely to FAIL")
