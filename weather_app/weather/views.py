from django.shortcuts import render


def index(request):
    return render(request, 'weather/index.html')


def detail(request):
    return render(request, 'weather/detail.html')
