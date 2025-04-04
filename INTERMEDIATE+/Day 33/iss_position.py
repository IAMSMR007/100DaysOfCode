import requests
from datetime import datetime
import time

# 1. Get ISS current position
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])

# 2. Get sunrise and sunset times for my location
my_lat = 51
my_lng = -0.5
parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}

response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()

# Fix: Use data_sun instead of data, and correct variable names
sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

# 3. Compare the ISS position with my location
def is_iss_overhead():
    if (my_lat - 5 <= iss_lat <= my_lat + 5) and (my_lng - 5 <= iss_lng <= my_lng + 5):
        if time_now >= sunset or time_now <= sunrise:  # Check if it's dark
            return True
    return False

# Test the function
while True:
    time.sleep(60)  

    if is_iss_overhead():
        print("Look up! The ISS is above you in the night sky!")
    else:
        print("ISS is not overhead or it's daytime.")