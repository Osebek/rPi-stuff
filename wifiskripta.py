import subprocess
import requests
import json


PHONE_MAC_ADDR = "54:72:4f:1a:73:1c"
PHONE_MAC_ADDR_NEJC =  '34:4d:f7:37:c3:ef'


def stalkeralert(title, message):
	headers = {'Content-Type': 'application/json', 'Access-Token': 'o.41fB3y7w8W3gCw0PnCUY4NlIvAUHyryE' }
	payload = {'type': 'note', 'title': title, 'body': message}
	r = requests.post('https://api.pushbullet.com/v2/pushes', data = json.dumps(payload), headers=headers)

def readFromFile(fileName):
    with open(fileName) as f:
        array = []
        for line in f:
            array.append(line.rstrip('\n'))
    return array

def linesToMacIP(vrstice):
    del vrstice[0]
    del vrstice[0]
    mac_ip_table = []
    for vrstica in vrstice:
        mac_ip_table.append(vrstica.strip().split(" "))
    return mac_ip_table

def phoneConnected(connectedDevices):
    for device in connectedDevices:
        if device[0] == PHONE_MAC_ADDR :
            return True
    return False
lastCheck = True
while True:
    subprocess.call("./neighbourhood1.py > network_connections.txt", shell=True)
    vrstice = readFromFile("network_connections.txt")
    if phoneConnected(linesToMacIP(vrstice)):
    	if lastCheck == False:
		stalkeralert("GINGER ALERT", "Veronika je tle, alert alert alert")
		lastCheck = True
    else:
        lastCheck = False





