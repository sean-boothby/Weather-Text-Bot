import requests
import config

def checkweather(apikey):
    r = requests.get('https://api.darksky.net/forecast/'+ apikey + '/29.424349,-98.491142')
    r = r.json()
    lat = r["latitude"]
    lon = r["longitude"]
    current = r["currently"]
    descrip = current["summary"]
    stormdist = current["nearestStormDistance"]
    precip = current["precipIntensity"]
    rainchance = current["precipProbability"]
    temp = current["temperature"]
    sun = current["uvIndex"]
    item = [lat,lon,descrip,stormdist,precip,rainchance,temp,sun]


    text = str('The weather for you right now Mr.Boothby Latitude: {} Longitude: {}  Weather description: {} Distance to nearest storm: {} Precipitation: {} Chance of precip: {} Temperature: {} UV Factor: {}'.format(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
    return text


text = checkweather(config.API_KEY)
print(text)

