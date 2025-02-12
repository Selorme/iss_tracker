import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import os

load_dotenv()

MY_LAT = os.environ["MY_LAT"]
MY_LONG = os.environ["MY_LONG"]
MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]


def right_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# If the ISS is close to my current position
# and it is currently dark


def it_is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    sunrise_hour_utc_plus_3 = (sunrise + 3) % 24
    sunset_hour_utc_plus_3 = (sunset + 3) % 24

    time_now = datetime.now().hour

    if time_now <= sunrise_hour_utc_plus_3 or time_now >= sunset_hour_utc_plus_3:
        return True


while True:
    # Then send me an email to tell me to look up.
    if right_iss_position and it_is_dark:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg=f"Subject: Go see the ISS!\n\nStep outside and see the ISS!")
    # BONUS: run the code every 60 seconds.
    time.sleep(60)

