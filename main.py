import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL_JORD")
my_password = os.getenv("EMAIL_PASSWORD")
api = os.getenv("API_CLIMA")
my_gf_email = os.getenv("EMAIL_CYNT")


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

def jundiaiClima():
    weather_params_jund = {
        "lat": -23.187080,
        "lon": -46.884048,
        "cnt": 5,
        "appid": api,
    }
    reponse_jund = requests.get(OWM_Endpoint, params=weather_params_jund)
    weather_jundiai = reponse_jund.json()
    rain_jund = False
    for hour in weather_jundiai["list"]:
        if hour["weather"][0]["id"] < 700:
            rain_jund = True

    if rain_jund:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg='Subject:Aleta de chuva!\n\nVai chover hoje, se liga!!')
            connection.close()


def fortalClima():
    weather_params_fort = {
        "lat": -3.7172200,
        "lon": -38.5430600,
        "cnt": 4,
        "appid": api,
    }
    reponse_fort = requests.get(OWM_Endpoint, params=weather_params_fort)
    weather_fort = reponse_fort.json()
    rain_fort = False
    for hour in weather_fort["list"]:
        if hour["weather"][0]["id"] < 700:
            rain_fort = True

    if rain_fort:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_gf_email,
                                msg='Subject:Aleta de chuva!\n\nVai chover hj minha gatinha, leva um guarda chuva!\nAtenciosamente, Jordan S2')
            connection.close()
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_gf_email,
                                msg='Subject:Dia de Sol!\n\nHoje vai ser um dia gostoso de Sol em Fortaleza, aproveita gatinha!\nAtenciosamente, Jordan S2')
            connection.close()


jundiaiClima()
fortalClima()




