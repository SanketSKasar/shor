from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save(request):
    response = request.POST
    unit = Unit.objects.get(id = request.POST.get("id"))
    obs = Observation(Unit = unit, intensity = request.POST.get("intensity"), timestamp = request.POST.get("timestamp"))
    obs.save()
    return HttpResponse(status=200)

@csrf_exempt
def get(request):
    response = request.POST
    obss = Observation.objects.filter(Unit__ID=request.POST.get(id))
    return HttpResponse(obss)