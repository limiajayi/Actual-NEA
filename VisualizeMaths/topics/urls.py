from django.urls import path
from . import views
import students.views

urlpatterns = [
    path('dash/', students.views.dash, name='dash'), #URL which lets the topic app have access to student dash
    path('', views.subject, name='subject'), #URL that points to views.subject which returns the subject page
    path('quadratics/', views.quadratics, name='quadratics'), #URL pointing to views.quadratics which returns info on quadratics topic
    path('quadraticQs/', views.quadraticsQuestions, name='quadraticQs'), # URL pointing to the question page on quadratics
]