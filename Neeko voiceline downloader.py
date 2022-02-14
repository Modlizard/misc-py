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

def downloadSound(url):
    global hdr
    global linkID
    global x
    req = urllib.request.Request(url, headers=hdr)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8') #Downloading full website code to regex find the direct image link below
    directLinks = re.findall('https:\/\/static\.wikia\.nocookie\.net\/leagueoflegends\/images\/.\/..\/Neeko\..{1,20}\.ogg\/revision\/latest\?cb\=[0-9]{14}', respData)
   
    for x in range(len(directLinks)):
        with open(f"voicelines/a{x}.ogg", "wb+") as currentSoundFile:
            response = requests.get(directLinks[x])
            currentSoundFile.write(response.content) #Uses requests module to get the binary data of the online image and overwrite a generated local image with it
            print(f'Downloaded {x}')

downloadSound("https://leagueoflegends.fandom.com/wiki/Neeko/LoL/Audio")

print('FINISHED SUCCESSFULY')

