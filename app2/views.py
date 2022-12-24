from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mounika(request):
    return HttpResponse('<h1>mounika is good girl</h1>')