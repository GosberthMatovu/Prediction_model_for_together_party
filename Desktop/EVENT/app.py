import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.joblib')

# Title and description
st.title("📊 Class Size Prediction for ETE 1 and ETE 2 Together Party")
st.markdown("""
Welcome to the Class Size Prediction app! This tool helps you predict the expected class size for an event combining ETE 1 and ETE 2 based on several factors.
Fill out the information below and click 'Predict Class Size' to get an estimate.
""")

# Create columns for better layout
col1, col2 = st.columns(2)

# Input fields
with col1:
    previous_attendance_ete1 = st.slider("Previous Attendance (ETE 1)", min_value=50, max_value=200, value=100)
    previous_attendance_ete2 = st.slider("Previous Attendance (ETE 2)", min_value=50, max_value=200, value=100)
    marketing_effort = st.number_input("Marketing Effort (in TZshs)", min_value=100000, max_value=1000000, value=500000, step=50000)

with col2:
    event_date = st.selectbox("Event Date", ["Weekday", "Weekend"])
    guest_speakers = st.slider("Number of Guest Speakers", min_value=1, max_value=5, value=2)
    weather_forecast = st.selectbox("Weather Forecast", ["Sunny", "Rainy", "Cloudy"])
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening"])

# Prepare input data
input_data = pd.DataFrame({
    'Previous_Attendance_ETE1': [previous_attendance_ete1],
    'Previous_Attendance_ETE2': [previous_attendance_ete2],
    'Event_Date': [event_date],
    'Marketing_Effort': [marketing_effort],
    'Guest_Speakers': [guest_speakers],
    'Weather_Forecast': [weather_forecast],
    'Time_of_Day': [time_of_day]
})

# Prediction button
if st.button("Predict Class Size"):
    prediction = model.predict(input_data)
    # Round the prediction to the nearest whole number
    rounded_prediction = round(prediction[0])
    st.success(f"🎉 Predicted Class Size: {rounded_prediction}")

# Footer
st.markdown(""" By GROUP MEMBERS :  
            AMBROSIA MGHANI, AHMED MAULID, GEOFREY DISMAS AND GOSBERTH GORDIAN
""")
