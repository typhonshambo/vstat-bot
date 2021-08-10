import aiohttp
import asyncio
import json
import requests
import re

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








async def profile_stats(username, tagline):
    

    profile_api = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tagline}"
    async with aiohttp.ClientSession() as session:
        async with session.get(profile_api, json={}) as r:
            data = (await r.json())["data"]

    user = data["platformInfo"]["platformUserIdentifier"]
    avatarUrl = data["platformInfo"]["avatarUrl"]

    stats = data["segments"][0]["stats"]
    wins = stats["matchesWon"]["displayValue"]
    losses = stats["matchesLost"]["displayValue"]
    win_pct = stats["matchesWinPct"]["displayValue"]
    hs_pct = stats["headshotsPercentage"]["displayValue"]
    kd_ratio = stats["kDRatio"]["displayValue"]
    damagePerRound = stats["damagePerRound"]["displayValue"]
    time_played = stats["timePlayed"]["displayValue"]
    rank = stats["rank"]["metadata"]["tierName"]
    rankIconUrl = stats["rank"]["metadata"]["iconUrl"]

    DATA = dict(
        user=user,
        avatarUrl=avatarUrl,
        wins=wins,
        losses=losses,
        win_pct=win_pct,
        hs_pct=hs_pct,
        kd_ratio=kd_ratio,
        damagePerRound=damagePerRound,
        time_played=time_played,
        rank=rank,
        rankIconUrl=rankIconUrl,
    )

    return DATA

