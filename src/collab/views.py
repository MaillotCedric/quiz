from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from collab.models import test, Participer

def index(request):
    return HttpResponse(Participer.objects)