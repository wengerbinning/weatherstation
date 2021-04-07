from django.shortcuts import render
from django.http.response import JsonResponse

from .models import Station, Weather

# Create your views here.
def index(request):
    return render(request,"pull.html")

def pull(request):
    stations = Station.objects.all()
    station = stations[0]
    weathers_ = station.weather_set.all()
    weathers = {
        weather.id: {
            'station':weather.station.station_id,
            'date': weather.date,
            'time': weather.time,
            'speed': weather.speed,
            'direction': weather.direction,
            'temperature': weather.temperature,
            'humidity':weather.humidity, 
        }
        for weather in weathers_
    }
    return JsonResponse(weathers, safe=False)

def push(request, weather):
    pass