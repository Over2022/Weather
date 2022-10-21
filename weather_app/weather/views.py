from django.shortcuts import render
import requests


def index(request):
    appid = '2c619c63181e61385cbf2c53c504b559'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'Москва'
    res = requests.get(url.format(city)).json()

    city_info = {'city': city, 'temp': res['main']['temp'], 'icon': res['weather'][0]['icon'],
                 'temp_max': res['main']['temp_max'], 'temp_min': res['main']['temp_min'],
                 'humidity': res['main']['humidity']}
    context = {'info': city_info}
    return render(request, 'weather/index.html', context)


def detail(request):

    return render(request, 'weather/detail.html')
