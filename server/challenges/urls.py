from django.urls import path
from . import views # import the views file from the same directory

urlpatterns = [
    # Example of a url configuration, route is '/challenges/january', controller is function called index from views file 
    # '/challenges' part of the route is set up in the project (server directory) urls.py file. Think of this as a sub-route -- abstraction
    path('january', views.index),
    path('february', views.feb),
    path('<month>', views.monthly_challenge) # dynamic path segment uses <>, anything req params are passed to the monthly_challenge function as an argument
]