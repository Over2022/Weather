from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = '2c619c63181e61385cbf2c53c504b559'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    if request.method == 'GET':
        cities = City.objects.all().delete()

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {'city': city, 'temp': res['main']['temp'], 'icon': res['weather'][0]['icon'],
                 'temp_max': res['main']['temp_max'], 'temp_min': res['main']['temp_min'],
                 'humidity': res['main']['humidity']}
        all_cities.append(city_info)
        print(all_cities)

    context = {'all_cities': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


def detail(request):

    return render(request, 'weather/detail.html')
