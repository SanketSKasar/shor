from django.shortcuts import render
from .models import *

def save(request):
    response = request.POST
    unit = Unit.objects.get(ID = request["id"])
    obs = Observation(Unit = unit, intensity = request["intensity"], timestamp = request["timestamp"])
    obs.save()
    return HttpResponse(status=200)

def get(request):
    response = request.POST
    obss = Observation.objects.filter(Unit__ID=request[id])
    return HttpResponse(obss)