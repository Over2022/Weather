from django.shortcuts import render
import requests


def index(request):
    appid = '2c619c63181e61385cbf2c53c504b559'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'Moskva'
    res = requests.get(url.format(city))

    print(res.text)
    return render(request, 'weather/index.html')


def detail(request):
    return render(request, 'weather/detail.html')
