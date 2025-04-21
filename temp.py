import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your own API key
API_KEY = "2c8a16745f1b498522d1bf309dd701dc"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(URL)

# Check the status code of the response
if response.status_code == 200:
    data = response.json()
    
    # Print the raw data to inspect its structure
    print(data)
    
    # Check if 'list' is in the response
    if 'list' in data:
        forecast_list = data['list']
        weather_data = {
            "Datetime": [],
            "Temperature (°C)": []
        }

        for entry in forecast_list:
            dt = datetime.fromtimestamp(entry['dt'])
            temp = entry['main']['temp']
            weather_data["Datetime"].append(dt)
            weather_data["Temperature (°C)"].append(temp)

        # Create DataFrame
        df = pd.DataFrame(weather_data)

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(df["Datetime"], df["Temperature (°C)"], marker='o')
        plt.title(f"Temperature Forecast for {CITY}")
        plt.xlabel("Datetime")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print("Error: 'list' key not found in the response data.")
else:
    print(f"Error: Unable to fetch data. HTTP Status code: {response.status_code}")