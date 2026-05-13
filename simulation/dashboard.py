import streamlit as st
import random
import pandas as pd
import joblib
from datetime import datetime

# Load ML model
model = joblib.load("model/model.pkl")

# Load label encoder
label_encoder = joblib.load("model/label_encoder.pkl")

# Page title
st.title("Predictive Maintenance Dashboard")

st.subheader("Live Machine Monitoring System")

# Generate live sensor data
temperature = random.randint(25, 80)
vibration = round(random.uniform(0.1, 2.0), 2)
sound = random.randint(20, 120)

# Create dataframe
live_data = pd.DataFrame({
    "temperature": [temperature],
    "vibration": [vibration],
    "sound": [sound]
})

# Predict machine condition
prediction = model.predict(live_data)

# Decode label
status = label_encoder.inverse_transform(prediction)[0]

# Timestamp
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display timestamp
st.write(f"Timestamp: {current_time}")

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Temperature", f"{temperature} °C")
col2.metric("Vibration", vibration)
col3.metric("Sound Level", f"{sound} dB")

# Status alerts
if status == "Critical":
    st.error(f"Machine Status: {status}")
    st.error("ALERT: Immediate maintenance required!")

elif status == "Warning":
    st.warning(f"Machine Status: {status}")
    st.warning("WARNING: Machine condition degrading.")

else:
    st.success(f"Machine Status: {status}")

# Refresh button
st.button("Refresh Live Data")