from django.urls import path
from . import views # import the views file from the same directory

urlpatterns = [
    # Example of a url configuration, route is '/challenges/january', controller is function called index from views file 
    # '/challenges' part of the route is set up in the project (server directory) urls.py file. Think of this as a sub-route -- abstraction
    # dynamic path segment uses <>, anything req params are passed to the monthly_challenge function as an argument
    # Adding a data type to the dynamic path segment: <str:month> -- this is a string data type -- input validation
    # Order of the url patterns matters, Django will go through the list of url patterns and use the first one that matches the route
    path('hello_world', views.hello_world),
    path('test', views.test),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge),
]

