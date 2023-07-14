import json
import requests
import pandas as pd


#def get_weather():
def get_weather(beach_name, lat, lon):

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
        'Nome da Praia':                str(beach_name),
        'Cidade':                       str(doc['location']['name']),
        'Região':                       str(doc['location']['region']),
        'País':                         str(doc['location']['country']),
        'latitude':                     float(doc['location']['lat']),
        'longitude':                    float(doc['location']['lon']),
        
        'Temperatura (ºC)':             float(doc['current']['temp_c']),
        'Velocidade do Vento (km/h)':   float(doc['current']['wind_kph']),
        'Raios UV':                     doc['current']['uv'],
        'Última Atualização':           doc['current']['last_updated'],
        
        'Condição Climática':           str(doc['current']['condition']['text']),
        'Code':                         int(doc['current']['condition']['code'])


    }
    return df_raw