#er mag maar 300 Calls worden gemaakt naar de API van Marvel. Niet dat we dat zullen halen in een dag...

import time 
import hashlib  
import json
import requests #deze library staat er niet standaard in. Voor python3 moet je (macOS) pip3 install requests gebruiken
                #voor Windows is het hetzeflde maar dat moet dan met PuTTy

timestamp = str(time.time())
private_key = "cad405dd110185a5a32b343035dea88e85cf81c5" #Deze Public en Private keys zijn gegenereerd door Marvel.
public_key = "637ca0492db6d09597f579a21bf6bd10"          #Daarvoor is een account nodig.

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') ) 
md5digest = str(hash.hexdigest())

url = "http://gateway.marvel.com:80/v1/public/characters" 
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest 
print(connection_url)

response = requests.get(connection_url) 
jsontext = json.loads(response.text)

# om de JSON leesbaar te printen... 
print(json.dumps(jsontext, sort_keys=True, indent=4))
print("\nGevonden characters in comics:") 

# JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs! 
for item in jsontext['data']['results'][0]['comics']['items']: 
    print(item['name'])

# volgende stappen zijn: 
# Tips laten tonen dmv bepaalde descriptions te laten zien of powers.
# punten systeem maken en ergen opslaan in een txt file.
# De data structureren om wat overzicht te maken.


