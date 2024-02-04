import requests
import json
tools = [ {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": { "type": "string", "description": "The city and state, e.g. San Francisco, CA", }
                    },
                    "required": ["location"],
                },
            },
        } ]

def get_current_weather(location):
    response = requests.get("http://api.weatherstack.com/current?access_key=<key>&query=" + location)
    data = response.json()
    current_weather = data['current']
    return json.dumps(current_weather);

      
