import requests

def get_uuid():
    r = requests.get("https://valorant-api.com/v1/weapons")
    puuid_raw = r.json()

    uuid_list = []
    name_list = []
    for i in range(len(puuid_raw["data"])):
        uuid_list.append(puuid_raw["data"][i]["uuid"])
        name_list.append(puuid_raw["data"][i]["displayName"])
        i += 1
    
    

    return uuid_list, name_list



def get_data(weaponUuid):
    r =  requests.get(f"https://valorant-api.com/v1/weapons/{weaponUuid}")
    data = r.json()

    displayIcon = data['data']['displayIcon']
    killStreamIcon = data['data']['killStreamIcon']


    fireRate = data['data']['weaponStats']['fireRate']
    magazineSize = data['data']['weaponStats']['magazineSize']
    reloadTimeSeconds = data['data']['weaponStats']['reloadTimeSeconds']
    wallPenetration = data['data']['weaponStats']['wallPenetration'].split('::')
    cost = data['data']['shopData']['cost']


    damageRange0 = []
    damageRange1 = []
    damageRange2 = []

    try: 

        damageRange0.append(data['data']['weaponStats']['damageRanges'][0]['rangeStartMeters'])
        damageRange0.append(data['data']['weaponStats']['damageRanges'][0]['rangeEndMeters'])
        damageRange0.append(data['data']['weaponStats']['damageRanges'][0]['headDamage'])
        damageRange0.append(data['data']['weaponStats']['damageRanges'][0]['bodyDamage']) 
        damageRange0.append(data['data']['weaponStats']['damageRanges'][0]['legDamage'])

        damageRange1.append(data['data']['weaponStats']['damageRanges'][1]['rangeStartMeters'])
        damageRange1.append(data['data']['weaponStats']['damageRanges'][1]['rangeEndMeters'])
        damageRange1.append(data['data']['weaponStats']['damageRanges'][1]['headDamage'])
        damageRange1.append(data['data']['weaponStats']['damageRanges'][1]['bodyDamage']) 
        damageRange1.append(data['data']['weaponStats']['damageRanges'][1]['legDamage'])

        damageRange2.append(data['data']['weaponStats']['damageRanges'][2]['rangeStartMeters'])
        damageRange2.append(data['data']['weaponStats']['damageRanges'][2]['rangeEndMeters'])
        damageRange2.append(data['data']['weaponStats']['damageRanges'][2]['headDamage'])
        damageRange2.append(data['data']['weaponStats']['damageRanges'][2]['bodyDamage']) 
        damageRange2.append(data['data']['weaponStats']['damageRanges'][2]['legDamage'])
    except:
        pass


    whole_data = {
        "displayIcon" : displayIcon,
        "killStreamIcon" : killStreamIcon,
        "fireRate": fireRate,
        "magazineSize" : magazineSize,
        "reloadTimeSeconds" : reloadTimeSeconds,
        "wallPenetration" : wallPenetration[1],
        "cost" : cost,
        "damageRange0" : damageRange0,
        "damageRange1" : damageRange1,
        "damageRange2" : damageRange2

    }
    
    return whole_data





