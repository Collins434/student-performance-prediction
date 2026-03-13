import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# -----------------------------
# Login Page
# -----------------------------
st.set_page_config(page_title="Student Performance Prediction", layout="centered")
st.title("🎓 Student Performance Prediction System")

# Simple login credentials
users = {"admin": "1234", "student": "abcd"}

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.subheader("🔒 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and password == users[username]:
            st.session_state.login = True
            st.success("Logged in successfully!")
        else:
            st.error("Incorrect username or password")
    st.stop()

# -----------------------------
# Input Student Data
# -----------------------------
st.subheader("Enter Student Details Manually")
hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, value=5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.number_input("Previous Exam Score", 0, 100, 60)

student_data = pd.DataFrame({
    "Hours Studied": [hours_studied],
    "Attendance": [attendance],
    "Previous Score": [previous_score]
})

st.write("### Input Data", student_data)

# -----------------------------
# CSV Upload
# -----------------------------
st.subheader("Or Upload CSV File for Multiple Students")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df)
else:
    df = student_data.copy()

# -----------------------------
# Machine Learning Model
# -----------------------------
st.subheader("Predicted Performance")

# For demo, create a simple ML model on-the-fly
# In real project, train on historical data
X = df[["Hours Studied", "Attendance", "Previous Score"]]
y = (df["Hours Studied"]*3 + df["Attendance"]*0.3 + df["Previous Score"]*0.5).values  # demo target

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
predictions = model.predict(X)
df["Predicted Score"] = np.round(predictions, 2)

st.write(df)

# -----------------------------
# Visualization
# -----------------------------
st.subheader("📊 Performance Chart")
fig, ax = plt.subplots()
ax.bar(df.index - 0.2, df["Previous Score"], width=0.4, label="Previous Score", color="blue")
ax.bar(df.index + 0.2, df["Predicted Score"], width=0.4, label="Predicted Score", color="green")
ax.set_xlabel("Student Index")
ax.set_ylabel("Score")
ax.set_title("Previous vs Predicted Score")
ax.legend()
st.pyplot(fig)

st.success("✅ Prediction Completed Successfully!")
