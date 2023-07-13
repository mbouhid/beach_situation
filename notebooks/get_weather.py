import json
import requests
import pandas as pd


#def get_weather():
def get_weather(lat, lon):

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    #lat_lon = '"' + lat + ', ' + lon + '"'
    lat_lon = lat + ', ' + lon
    #querystring = {"q":"41.51735867793759, -8.787637816243148"}
    querystring = {"q":lat_lon}

    headers = {
        "X-RapidAPI-Key": "b1f8269ad8msh8a7ba18e18ad63dp14f463jsn998121aa0db7",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    #print(response.json())

    doc = response.json()

    df_raw = {
        'beach_name':         doc['location']['name'],
        'region':             doc['location']['region'],
        'country':            doc['location']['country'],
        'lat':                doc['location']['lat'],
        'lon':                doc['location']['lon'],
        
        'temp_c':             doc['current']['temp_c'],
        'wind_kph':           doc['current']['wind_kph'],
        'uv':                 doc['current']['uv'],
        'last_updated':       doc['current']['last_updated'],
        
        'condition':          doc['current']['condition']['text']


    }
    return df_raw