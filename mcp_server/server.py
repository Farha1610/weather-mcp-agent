from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "31456631bcf4b295b9acd76abaf5dcec"

@app.get("/weather")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "description": res["weather"][0]["description"]
    }