import requests
import smtplib

my_email = "jordan.pinheiro2005@gmail.com"


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "5bacae889c8f9f3f8379f6204760b13d"

weather_params = {
    "lat": -23.187080,
    "lon": -46.884048,
    "cnt": 4,
    "appid": api_key,
}

reponse_jund = requests.get(OWM_Endpoint, params=weather_params)

weather_jundiai = reponse_jund.json()
rain_jund = False

for hour in weather_jundiai["list"]:
    if hour["weather"][0]["id"] < 700:
        rain_jund = True

if rain_jund:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password='')
    connection.sendmail(from_addr=my_email, to_addrs="jordan.pinheiro2005@gmail.com", msg='Vai chover hoje, se liga!!')
    connection.close()





