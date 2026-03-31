import requests

MCP_URL = "https://weather-agent-447034330708.asia-south1.run.app/weather"

def weather_agent(query):
    if "weather" in query.lower():
        city = query.split()[-1]

        response = requests.get(MCP_URL, params={"city": city}).json()

        return f"The weather in {response['city']} is {response['description']} with {response['temperature']}°C."

    return "Sorry, I can only answer weather-related questions."