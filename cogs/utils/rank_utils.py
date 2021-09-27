import  requests


def getrank(region, user_id):
    req_data = requests.get(f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/{region}/{user_id}") 
    whole_data = req_data.json()

    
    return whole_data