import urllib.request as urllib
import json

def bundle_list(link):
    url = urllib.urlopen(link)
    bundles_list = []
    j = json.loads(url.read())
    for i in range(len(j["data"])):
        data = (j["data"][i]["displayName"])
        bundles_list.append(data)

    str_list = ""
    str_list.join(bundles_list)

    str1 = "▫"+"""\n▫""".join(str(e) for e in bundles_list)
    
    return str1


def bundle_list_img(link):
    url = urllib.urlopen(link)
    bundles_list = []
    j = json.loads(url.read())
    for i in range(len(j["data"])):
        data = (j["data"][i]["displayName"])
        bundles_list.append(data)
    return bundles_list

def bundle_get_image(link, i):
    url = urllib.urlopen(link)
    bundles_img = ""
    j = json.loads(url.read())
    data = (j["data"][i]["displayIcon"])
    bundles_img += data 
    return bundles_img


