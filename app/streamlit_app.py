import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/placement_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Placement Prediction System")
st.markdown("Predict whether a student is likely to get placed based on academic performance and skills.")

# ---------------------------
# SLIDER INPUTS
# ---------------------------
st.sidebar.header("Slider Inputs")

cgpa_slider = st.sidebar.slider("CGPA", 0.0, 10.0, 7.0)

programming_slider = st.sidebar.slider("Programming Skills", 1, 10, 5)
communication_slider = st.sidebar.slider("Communication Skills", 1, 10, 5)

projects_slider = st.sidebar.slider("Projects Completed", 0, 10, 2)
internship_slider = st.sidebar.slider("Internship Experience", 0, 5, 1)

attendance_slider = st.sidebar.slider("Attendance (%)", 0, 100, 75)
backlogs_slider = st.sidebar.slider("Number of Backlogs", 0, 10, 0)

# ---------------------------
# MANUAL INPUT SECTION
# ---------------------------
st.subheader("✍️ Manual Input (Optional)")

col1, col2 = st.columns(2)

with col1:
    cgpa_manual = st.number_input("CGPA", 0.0, 10.0, cgpa_slider)
    programming_manual = st.number_input("Programming Skills", 1, 10, programming_slider)
    communication_manual = st.number_input("Communication Skills", 1, 10, communication_slider)
    projects_manual = st.number_input("Projects Completed", 0, 10, projects_slider)

with col2:
    internship_manual = st.number_input("Internship Experience", 0, 5, internship_slider)
    attendance_manual = st.number_input("Attendance (%)", 0, 100, attendance_slider)
    backlogs_manual = st.number_input("Backlogs", 0, 10, backlogs_slider)

# ---------------------------
# CREATE DATAFRAME
# ---------------------------
input_data = pd.DataFrame({
    "CGPA": [cgpa_manual],
    "Programming_Skills": [programming_manual],
    "Communication_Skills": [communication_manual],
    "Projects_Completed": [projects_manual],
    "Internship_Experience": [internship_manual],
    "Attendance": [attendance_manual],
    "Backlogs": [backlogs_manual]
})

# Ensure correct feature order
input_data = input_data[model.feature_names_in_]

# Show student profile
st.subheader("📋 Student Profile")
st.dataframe(input_data)

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict Placement"):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.success("✅ The student is likely to be **PLACED**")
    else:
        st.error("❌ The student is likely **NOT to be placed**")

    st.subheader("🎯 Prediction Confidence")

    placement_prob = probability[0][1] * 100
    st.write(f"Placement Probability: **{placement_prob:.2f}%**")