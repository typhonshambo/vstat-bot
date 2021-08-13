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

async def GetMatchData(username , tagline):

    
    history_api = f"https://api.tracker.gg/api/v2/valorant/rap-matches/riot/{username}%23{tagline}"
    async with aiohttp.ClientSession() as session:
        async with session.get(history_api) as r:
            data = json.loads(await r.text())

    matches = data["data"]["matches"]
    for match in matches:
        if "modeName" in match["metadata"]:
            if match["metadata"]["modeName"] == "Competitive":
                return match["attributes"]["id"]
    return None

async def match_stats(match_id):
    match_api = f"https://api.tracker.gg/api/v2/valorant/rap-matches/{match_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(match_api, json={}) as r:
            data = (await r.json())["data"]

    MATCH_DATA = {}
    PLAYER_DATA = {}

    red_team = data["segments"][0]
    blue_team = data["segments"][1]
    players = data["segments"][2:12]

    MATCH_DATA["match_info"] = {}
    MATCH_DATA["match_info"]["duration"] = data["metadata"]["duration"]
    MATCH_DATA["match_info"]["start"] = data["metadata"]["dateStarted"]
    MATCH_DATA["match_info"]["map_name"] = data["metadata"]["mapName"]
    MATCH_DATA["match_info"]["map_image_url"] = data["metadata"]["mapImageUrl"]

    MATCH_DATA["Red"] = {}
    MATCH_DATA["Red"]["rounds_won"] = red_team["stats"]["roundsWon"]["displayValue"]
    MATCH_DATA["Red"]["won"] = red_team["metadata"]["hasWon"]

    MATCH_DATA["Blue"] = {}
    MATCH_DATA["Blue"]["rounds_won"] = blue_team["stats"]["roundsWon"]["displayValue"]
    MATCH_DATA["Blue"]["won"] = blue_team["metadata"]["hasWon"]

    for player in players:
        metadata = player["metadata"]
        display_name = metadata["platformInfo"]["platformUserIdentifier"]
        team = metadata["teamId"]
        agent = metadata["agentName"]
        agentImageUrl = metadata["agentImageUrl"]

        stats = player["stats"]
        rank = stats["rank"]["displayValue"]
        score = stats["scorePerRound"]["displayValue"]
        kills = stats["kills"]["displayValue"]
        deaths = stats["deaths"]["displayValue"]
        assists = stats["assists"]["displayValue"]
        kdRatio = stats["kdRatio"]["displayValue"]
        damagePerRound = stats["damagePerRound"]["displayValue"]

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

    return MATCH_DATA, PLAYER_DATA





