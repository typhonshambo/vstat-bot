import requests

def getleaderboard(region , amount):
    raw_data = requests.get(f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}")
    data = raw_data.json()

    PLAYER_DATA = {}
    

    i = 0

    
    for i in range(0, amount):
        name = data[i]['gameName']
        tagLine = data[i]['tagLine']
        leaderboardRank = data[i]['leaderboardRank']
        numberOfWins = data[i]['numberOfWins']
        rankedRating = data[i]['rankedRating']
        
        PLAYER_DATA[i] = {}
        PLAYER_DATA[i]['name'] = name
        PLAYER_DATA[i]['tagLine'] = tagLine
        PLAYER_DATA[i]['leaderboard'] = leaderboardRank
        PLAYER_DATA[i]['numberOfWins'] = numberOfWins
        PLAYER_DATA[i]['rankedRating'] = rankedRating
        i += 1
    return PLAYER_DATA

