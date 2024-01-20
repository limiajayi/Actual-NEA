from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash, name='dash'), #the url pointing to views.dash which returns the student dash
    path('qform/', views.qform, name='qform'), #the url pointing to views.qform which returns a form allowing users to get questions
    path('logout/', views.logout, name='logout'), #the url pointing to views.logout which lets users logout
    path('question/', views.question, name='question'), #the url pointing to views.question which returns the question page
]