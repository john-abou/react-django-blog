from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for the entire month!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': 'Learn Django for at least 20 minutes every day!',
}

# Create your views here. Note, no need to export the views file or functions from the views file. 
# Django will find the views file and use the functions in it.
def hello_world(req):
    return HttpResponse('Hello, world. You are at the challenges index.')

def test(req):
    return HttpResponse('This is the February challenge.')

def monthly_challenge(req, month): # req is the request object, month is the dynamic path segment (req param(s) -- keyword arguments)
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')  


def monthly_challenge_by_number(req, month):
    forward_month_array = list(monthly_challenges.keys()) # Get a list of the keys of the monthly_challenges dictionary
    try:
        forward_month = forward_month_array[month - 1] # Get the month from the list of keys using the month param as the index

        # Use the reverse() function to get the url pattern for the month-challenge url pattern
        # This is the path to the month-challenge url pattern -- /challenges/<str:month>
        # Note, the reverse() function returns the path as a string
        redirect_path = reverse('month-challenge', args=[forward_month]) 

        #Redirect to the monthly_challenge view using the month as the dynamic path segment
        #Note, the re-direct is not relative to the current route, it is relative to the root route of the server (server/urls.py)
        # This is why we need to add the 'challenges/' part of the route to the redirect
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('This month is not supported!')  