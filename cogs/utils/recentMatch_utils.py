import requests
import re
from . import match_resource as res

def username_to_data(username, password):
    session = requests.session()
    data = {
        'client_id': 'play-valorant-web-prod',
        'nonce': '1',
        'redirect_uri': 'https://playvalorant.com/opt_in',
        'response_type': 'token id_token',
    }
    r = session.post('https://auth.riotgames.com/api/v1/authorization', json=data)

    data = {
        'type': 'auth',
        'username': username,
        'password': password
    }
    r = session.put('https://auth.riotgames.com/api/v1/authorization', json=data)
    pattern = re.compile(
        'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
    data = pattern.findall(r.json()['response']['parameters']['uri'])[0]
    access_token = data[0]

    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    r = session.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={})
    entitlements_token = r.json()['entitlements_token']

    r = session.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
    user_id = r.json()['sub']

    session.close()
    return [access_token, entitlements_token, user_id]


def getingamename(region, user_id):
    req_data = requests.get(f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/{region}/{user_id}") 
    whole_data = req_data.json()

    
    
    return whole_data

async def GetMatchData(region, user_id):

    
    history_api = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{user_id}")
    data = history_api.json()

    try:
        matches = data["data"][0]["metadata"]
        return matches["matchid"]
    except:
        return None




def matchStat(match_id):
    match_api = requests.get(f" https://api.henrikdev.xyz/valorant/v2/match/{match_id}")
    data = match_api.json()

    MATCH_DATA = {}
    PLAYER_DATA = {}

    red_team = data["data"]["teams"]["red"]
    blue_team =  data["data"]["teams"]["blue"]
    players = data["data"]["players"]["all_players"][0:10]
    i = 0 

    MATCH_DATA["match_info"] = {}
    MATCH_DATA["match_info"]["map_name"] = data["data"]["metadata"]["map"]
    MATCH_DATA["match_info"]["start"] = data["data"]["metadata"]["game_start_patched"]

    MATCH_DATA["Red"] = {}
    MATCH_DATA["Red"]["rounds_won"] = red_team["rounds_won"]
    MATCH_DATA["Red"]["won"] = red_team["has_won"]

    MATCH_DATA["Blue"] = {}
    MATCH_DATA["Blue"]["rounds_won"] = blue_team["rounds_won"]
    MATCH_DATA["Blue"]["won"] = blue_team["has_won"]
    
    for player in players:
        
        display_username = players[i]["name"]
        display_tag = players[i]["tag"]

        display_name = display_username + display_tag
        team = players[i]["team"]
        agent = players[i]["character"]
        agentImageUrl = res.agent_img[f"{agent}"]
        rank = players[i]["currenttier_patched"]

        stats = player["stats"]
        score = stats["score"]
        kills = stats["kills"]
        deaths = stats["deaths"]
        assists = stats["assists"]
        kdRatio_cal = kills/deaths
        kdRatio = round(kdRatio_cal , 2)
       

        
        PLAYER_DATA[display_name] = {}
        PLAYER_DATA[display_name]["team"] = team
        PLAYER_DATA[display_name]["agent"] = agent
        PLAYER_DATA[display_name]["agent_image_url"] = agentImageUrl
        PLAYER_DATA[display_name]["rank"] = rank
        PLAYER_DATA[display_name]["score"] = score
        PLAYER_DATA[display_name]["kills"] = kills
        PLAYER_DATA[display_name]["deaths"] = deaths
        PLAYER_DATA[display_name]["assists"] = assists
        PLAYER_DATA[display_name]["kd_ratio"] = kdRatio

        i += 1
    
    return MATCH_DATA, PLAYER_DATA

