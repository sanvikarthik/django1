from django.shortcuts import render
import datetime
from django.http import HttpResponse

def cdt(request):
    dt = datetime.datetime.now()
    resp = "<h1>Current Date and Time is %s</h1>" % dt
    return HttpResponse(resp)

def aheadtime(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=4)
    resp = "<html><head><title>Current Time Ahead by 4hrs</title></head><body><h1>Current date and Time ahead by 4 hrs is %s</h1></body></html>" % dt
    return HttpResponse(resp)

def home(request):
    resp = "<h1>Welcome to the Home Page</h1>"
    return HttpResponse(resp)

def beforetime(request): 
    dt=datetime.datetime.now()+datetime.timedelta(hours=-4) 
    resp="<h1>Current Server Date and Time Before 4hrs is %s</h1>"%(dt) 
    return HttpResponse(resp)