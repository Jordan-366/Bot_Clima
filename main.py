import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL_JORD")
my_password = os.getenv("EMAIL_PASSWORD")
api = os.getenv("API_CLIMA")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": -23.187080,
    "lon": -46.884048,
    "cnt": 4,
    "appid": api,
}

reponse_jund = requests.get(OWM_Endpoint, params=weather_params)

weather_jundiai = reponse_jund.json()
rain_jund = False

print(weather_jundiai)

for hour in weather_jundiai["list"]:
    if hour["weather"][0]["id"] < 700:
        rain_jund = True

if rain_jund:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg='Subject:Aleta de chuva!\n\nVai chover hoje, se liga!!')
        connection.close()





