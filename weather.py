import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')


message = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

def weather(promt):
    payload = {'q': promt,
               'appid': TOKEN
    }
    day_weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload).json()
    city_test = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=payload).json()
    if 'cod' in city_test or 'cod' in day_weather:
        if city_test['cod'] != '200' or day_weather['cod'] != 200:
            return False
    day_weather = [round(day_weather['main']['temp'] - 273.15), int(day_weather['dt'])]
    day = datetime.isoweekday(datetime.now())
    print('Сегодня: ', message[day])
    dict_weather, result_dict = {}, {}
    for i in city_test['list']:
        date = datetime.fromtimestamp(i['dt'])
        day_json = datetime.isoweekday(date)
        if day_json != day:
            if day_json not in dict_weather:
                dict_weather[day_json] = {'main': [], 'weather': []}
            dict_weather[day_json]['main'].append(i['main']['temp'])
            dict_weather[day_json]['weather'].append(i['weather'][0]['main'])

    for key, value in dict_weather.items():
        if value['main']:
            result_dict[message[key]] = {'max': round(max(value['main']) - 273.15),
                                         'weather': max(set(value['weather']), key=value['weather'].count)}

    return day_weather, result_dict

print(weather('Казань'))
