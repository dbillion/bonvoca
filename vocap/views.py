from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    return render(request, 'vocap/index.html')


def weather(request):
    city = 'London'
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    data = request.get(url).json()
    weather_data = {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    context = {'weather_data': weather_data}
    return render(request, 'weather.html', context)


def get_weather_data(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=your_api_key'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    return city_weather

def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:
        city_weather = get_weather_data(city.name)
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'vocap/weather.html', context)
