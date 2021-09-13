import json
import requests
import re
import aiohttp

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

    agent_icons={
    "Breach":"https://media.valorant-api.com/agents/5f8d3a7f-467b-97f3-062c-13acf203c006/displayicon.png",
    "Raze":"https://media.valorant-api.com/agents/f94c3b30-42be-e959-889c-5aa313dba261/displayicon.png",
    "KAY/O":"https://media.valorant-api.com/agents/601dbbe7-43ce-be57-2a40-4abd24953621/displayicon.png",
    "Skye":"https://media.valorant-api.com/agents/6f2a04ca-43e0-be17-7f36-b3908627744d/displayicon.png",
    "Cypher":"https://media.valorant-api.com/agents/117ed9e3-49f3-6512-3ccf-0cada7e3823b/displayicon.png",
    "Sova":"https://media.valorant-api.com/agents/ded3520f-4264-bfed-162d-b080e2abccf9/displayicon.png",
    "Killjoy":"https://media.valorant-api.com/agents/1e58de9c-4950-5125-93e9-a0aee9f98746/displayicon.png",
    "Viper":"https://media.valorant-api.com/agents/707eab51-4836-f488-046a-cda6bf494859/displayicon.png",
    "Phoenix":"https://media.valorant-api.com/agents/eb93336a-449b-9c1b-0a54-a891f7921d69/displayicon.png",
    "Astra":"https://media.valorant-api.com/agents/41fb69c1-4189-7b37-f117-bcaf1e96f1bf/displayicon.png",
    "Brimstone":"https://media.valorant-api.com/agents/9f0d8ba9-4140-b941-57d3-a7ad57c6b417/displayicon.png",
    "Yoru":"https://media.valorant-api.com/agents/7f94d92c-4234-0a36-9646-3a87eb8b5c89/displayicon.png",
    "Sage":"https://media.valorant-api.com/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png",
    "Reyna":"https://media.valorant-api.com/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/displayicon.png",
    "Omen":"https://media.valorant-api.com/agents/8e253930-4c05-31dd-1b6c-968525494517/displayicon.png",
    "Jett":"https://media.valorant-api.com/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png"
    }
    
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
        agentImageUrl = agent_icons[agent]
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

