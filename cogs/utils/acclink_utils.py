import requests

def accountData(name, tagline):
    r  = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{name}/{tagline}')
    data = r.json()

    puuid = data['data']['puuid']
    region = data['data']['region']

    return puuid, region

