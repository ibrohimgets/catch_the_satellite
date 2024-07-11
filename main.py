import requests
import smtplib
import time

# API URL and coordinates
API = "https://api.sunrisesunset.io/json"
LAT = 38.907192  # Latitude for Washington, D.C.
LON = -77.036873  # Longitude for Washington, D.C.

# Email setup
my_email = "ibrohimuminov@gmail.com"
app_passwords = "xlnt tyxo wuyp ckac"  # Replace with your generated app password

# Parameters for API request
parameters = {
    "lat": LAT,
    "lng": LON,
    "formatted": 0,  # Ensure we get the raw data
}

while True:
    try:
        # Fetch data from API
        response = requests.get(API, params=parameters)
        response.raise_for_status()
        data = response.json()

        # Check if the timezone is appropriate (e.g., "Asia/Seoul")
        timezone = data["results"]["timezone"]
        if "Seoul" in timezone:
            # Establish connection to SMTP server
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_passwords)

                # Compose the email
                subject = "The satellite position reminder!"
                body = "The satellite is somewhere above you!"
                message = f"Subject: {subject}\n\n{body}"

                # Send email
                to_addrs = ["iibrohimm.com@gmail.com", "961972398@qq.com"]
                connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg=message)
                print("It's just over your head!")

        # Sleep for 60 seconds before checking again
        time.sleep(60)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        time.sleep(60)  # Retry after 60 seconds

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        # Handle the error as needed, perhaps retrying or logging

    except Exception as e:
        print(f"Unexpected error: {e}")
        time.sleep(60)  # Retry after 60 seconds
