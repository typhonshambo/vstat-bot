import requests
import json

with open ('config\config.json', 'r') as f:
    config = json.load(f)
    auth_token = config['AUTH_TOKEN']


def getValorantInfo():
    URL = "https://na.api.riotgames.com/val/content/v1/contents?locale=en-US&api_key=" + auth_token

    response = requests.get(URL)
    return response.json()
