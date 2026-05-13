import random
import time
import joblib
import pandas as pd
from datetime import datetime
# Load trained model
model = joblib.load("model/model.pkl")

# Load label encoder
label_encoder = joblib.load("model/label_encoder.pkl")

while True:

    # Generate live sensor values
    temperature = random.randint(25, 80)
    vibration = round(random.uniform(0.1, 2.0), 2)
    sound = random.randint(20, 120)

    # Convert data into dataframe
    live_data = pd.DataFrame({
        "temperature": [temperature],
        "vibration": [vibration],
        "sound": [sound]
    })

    # Predict machine condition
    prediction = model.predict(live_data)

    # Decode prediction label
    status = label_encoder.inverse_transform(prediction)[0]

    # Display output
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n==============================")
    print("   LIVE MACHINE MONITORING")
    print(f"Timestamp     : {current_time}")
    print("==============================")
    print(f"Temperature   : {temperature} °C")
    print(f"Vibration     : {vibration}")
    print(f"Sound Level   : {sound} dB")
    print("------------------------------")
    print(f"Machine Status: {status}")

    if status == "Critical":
        print("ALERT: Immediate maintenance required!")

    elif status == "Warning":
        print("WARNING: Machine condition degrading.")

    print("==============================")

    time.sleep(3)