import requests
import time

def stream():
    response = requests.get("http://192.168.30.27/aircraftlist.json")
    data = response.json()
    for line in data:
        yield line

def getCurrentTime():
    print(time.ctime())

getCurrentTime()
data = stream()
for line in data:
    pass
getCurrentTime() 