from django.urls import path #an inbuilt django function used for routing urls to the appropriate views.py function
from . import views #a file that contains functions that take http requests and return the page corresponding to that request
import students.views #this file has the same function as the file above except it returns pages in the students app

urlpatterns = [
    path('dash/', students.views.dash, name='dash'), #URL which lets the topic app have access to student dash
    path('mathsSubject/', views.mathsSubject, name='maths'), #URL that points to views.subject which returns the subject page
    path('fmathsSubject/', views.furtherMathsSubject, name='furtherMaths'), #URL that points to views.subject which returns the subject page
    path('quadratics/', views.quadratics, name='quadratics'), #URL pointing to views.quadratics which returns info on quadratics topic
    path('quadraticQs/', views.quadraticsQuestions, name='quadraticQs'), # URL pointing to the question page on quadratics
    path('inequalities/', views.inequalities, name='inequalites'),
    path('transformations/', views.graphsTransformations, name='transformations'),
    path('straightLineGraphs/', views.straightLineGraphs, name='straightLineGraphs'),
    path('circles/', views.circles, name='circles'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('differentiation/', views.differentiation, name='differentiation'),
    path('integration/', views.integration, name='integration'),
    path('logarithms/', views.exponents, name='exponents'),
    path('2DVectors', views.twoDVectors, name='2DVectors'),
    path('3DVectors', views.threeDVectors, name='3DVectors'),
    path('argandDiagrams/', views.argandDiagrams, name='argandDiagrams'),
    path('volumesOfRevolution/', views.volumesOfRevolution, name='volumesOfRevolution'),
    path('methodsInCalculus/', views.methodsInCalculus, name='methodsInCalculus'),
    path('matrices/', views.matrices, name='matrices'),
    path('polarCoordinates/', views.polarCoordinates, name='polarCoordinates'),
    path('hyperbolics/', views.hyperbolic, name='hyperbolic'),
]