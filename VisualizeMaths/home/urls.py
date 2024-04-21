from django.urls import path #an inbuilt django function used for routing urls to the appropriate views.py function
from . import views #a file that contains functions that take http requests and return the page corresponding to that request

urlpatterns = [
    path('', views.home, name='home'), #the url pointing to views.home which returns the home page
    path('login/', views.login, name='login'), #url pointing to login page
    path('signup/', views.signup, name='signup'), #url pointing to views.signup which returns the signup page
]
