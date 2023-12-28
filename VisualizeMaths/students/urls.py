from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash, name='dash'), #the url pointing to views.dash which returns the student dash
    path('logout/', views.logout, name='logout'), #the url pointing to views.logout which lets users logout
]