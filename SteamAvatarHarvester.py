import urllib.request
import requests
import json
import math

filePath = '\\Desktop\\'
fileName = 'UNIQUE_SORTED_FIX_FriendsDepth2.json'
downloadPath = '\\Desktop\\steamIcons\\'
API = ''
massive = 100

fileContent = []
steamIDs = ''

history = ["https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/fe/fef49e7fa7e1997310d705b2a6158ff8dc1cdfeb.jpg", ""]

def apiPull(steamID):
    return urllib.request.urlopen('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key='+API+'&steamids='+steamID).read().decode('utf8')

def imgDL(url):
    r = requests.get(url, allow_redirects=True)
    with open(downloadPath + steamID_ + '.jpg', 'wb') as file:
        file.write(r.content)

with open(filePath + fileName) as file:
    fileContent = json.load(file)

print(len(fileContent))

for i in range(int(math.floor(len(fileContent)/massive))):
    if len(fileContent)%massive != 0:
        for i in range(len(fileContent)%massive):
            steamIDs += (str(fileContent.pop(0)) + '+')
        steamIDs = steamIDs[0:-1]
        page = apiPull(steamIDs)
        pull = json.loads(page)
        for i in (pull['response']['players']):
            steamID_ = i['steamid']
            if i['avatar'] not in history:
                imgDL(i['avatar'])
                history.append(i['avatar'])
    steamIDs = ''
    for i in range(massive):
        steamIDs += (str(fileContent.pop(0)) + '+')
    
    steamIDs = steamIDs[0:-1]
    page = apiPull(steamIDs)
    pull = json.loads(page)
    for i in (pull['response']['players']):
        steamID_ = i['steamid']
        if i['avatar'] not in history:
            imgDL(i['avatar'])
            history.append(i['avatar'])