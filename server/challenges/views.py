from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
def index(req):
    return HttpResponse('Hello, world. You are at the challenges index.')

def feb(req):
    return HttpResponse('This is the February challenge.')

def monthly_challenge(req, month): # req is the request object, month is the dynamic path segment (req param(s) -- keyword arguments)
    challenge_text = None
    if month == 'april':
        challenge_text = 'Eat no meat for the entire month!'
    elif month == 'may':
        challenge_text = 'Walk for at least 20 minutes every day!'
    elif month == 'june':
        challenge_text = 'Learn Django for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound('This month is not supported!')     
    
    return HttpResponse(challenge_text)