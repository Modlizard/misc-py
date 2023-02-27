import urllib.request
import re
import requests
import os

from datetime import datetime
now = datetime.now()
dt_string = now.strftime('%d/%m/%Y %H:%M:%S')

cwd = os.getcwd()

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'} #You get banned for being a 'bot' so we include user like headers

linkSuffixes = ['weapon/CZ75-Auto', 'weapon/Desert+Eagle', 'weapon/Dual+Berettas', 'weapon/Five-SeveN', 'weapon/Glock-18', 'weapon/P2000', 'weapon/P250', 'weapon/R8+Revolver', 'weapon/Tec-9', 'weapon/USP-S', 
'weapon/AK-47', 'weapon/AUG', 'weapon/AWP', 'weapon/FAMAS', 'weapon/G3SG1', 'weapon/Galil+AR', 'weapon/M4A1-S', 'weapon/M4A4', 'weapon/SCAR-20', 'weapon/SG+553', 'weapon/SSG+08', 
'weapon/MAC-10', 'weapon/MP5-SD', 'weapon/MP7', 'weapon/MP9', 'weapon/PP-Bizon', 'weapon/P90', 'weapon/UMP-45', 
'weapon/MAG-7', 'weapon/Nova', 'weapon/Sawed-Off', 'weapon/XM1014', 'weapon/M249', 'weapon/Negev', 
'weapon/Nomad+Knife', 'weapon/Skeleton+Knife', 'weapon/Survival+Knife', 'weapon/Paracord+Knife', 'weapon/Classic+Knife', 'weapon/Bayonet', 'weapon/Bowie+Knife', 'weapon/Butterfly+Knife', 'weapon/Falchion+Knife', 'weapon/Flip+Knife', 'weapon/Gut+Knife', 'weapon/Huntsman+Knife', 'weapon/Karambit', 'weapon/M9+Bayonet', 'weapon/Navaja+Knife', 'weapon/Shadow+Daggers', 'weapon/Stiletto+Knife', 'weapon/Talon+Knife', 'weapon/Ursus+Knife', 
'gloves', 'gloves?page=2']

weapons = ['CZ75-Auto', 'Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'P2000', 'P250', 'R8 Revolver', 'Tec-9', 'USP-S', 
'AK-47', 'AUG', 'AWP', 'FAMAS', 'G3SG1', 'Galil AR', 'M4A1-S', 'M4A4', 'SCAR-20', 'SG 553', 'SSG 08', 
'MAC-10', 'MP5-SD', 'MP7', 'MP9', 'PP-Bizon', 'P90', 'UMP-45', 
'MAG-7', 'Nova', 'Sawed-Off', 'XM1014', 'M249', 'Negev', 
'Nomad Knife', 'Skeleton Knife', 'Survival Knife', 'Paracord Knife', 'Classic Knife', 'Bayonet', 'Bowie Knife', 'Butterfly Knife', 'Falchion Knife', 'Flip Knife', 'Gut Knife', 'Huntsman Knife', 'Karambit', 'M9 Bayonet', 'Navaja Knife', 'Shadow Daggers', 'Stiletto Knife', 'Talon Knife', 'Ursus Knife',
'Gloves', 'Gloves']

def getWeaponData(url):
    global hdr
    req = urllib.request.Request(url, headers=hdr)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8') #Downloading full website code to regex find the direct image link below
    # The below consists of a src containing the image and alt text containing its name
    weaponData = re.findall('src=\"https:\/\/steamcdn-a\.akamaihd\.net\/apps\/730\/icons\/econ\/default_generated\/weapon_.+?light_large\.[a-f0-9]{40}\.png\" alt=\"[^\"]*\"', respData) # Ouputs list, use directLink[0] to get the string
    return weaponData
    # print('Downloaded prnt.sc/'+linkID+x)

for suffix, weapon in zip(linkSuffixes, weapons):
    weaponData = getWeaponData(f"https://csgostash.com/{suffix}")
    path = f'{cwd}\\{weapon}'
    if not os.path.exists(path):
        os.mkdir(path)
    for datum in weaponData:
        print(datum)
        datum = datum.split('"')
        url = datum[1]
        name = datum[3]
        with open(f"{weapon}/{name}.png", "wb+") as currentImg:
            pass
        urllib.request.urlretrieve(url, f"{weapon}/{name}.png")
    with open("Downloaded images.txt", "a+") as logFile:
        logFile.write(f"Downloaded all skins for {weapon} - {dt_string}\n")

print("===================FINISHED===================")
