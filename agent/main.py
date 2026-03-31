import requests

MCP_URL = "http://127.0.0.1:8000/weather"

def weather_agent(query):
    if "weather" in query.lower():
        city = query.split()[-1]

        response = requests.get(MCP_URL, params={"city": city}).json()

        return f"The weather in {response['city']} is {response['description']} with {response['temperature']}°C."

    return "Sorry, I can only answer weather-related questions."