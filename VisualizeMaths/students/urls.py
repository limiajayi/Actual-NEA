from django.urls import path
from . import views
import topics.views

urlpatterns = [
    path('dash/', views.dash, name='dash'), #the url pointing to views.dash which returns the student dash
    path('qform/', views.qform, name='qform'), #the url pointing to views.qform which returns a form allowing users to get questions
    path('logout/', views.logout, name='logout'), #the url pointing to views.logout which lets users logout
    path('questionMaths/', views.questionMaths), #the url pointing to views.questionMaths which returns the question page if a user is practising maths
    path('questionFurtherMaths/', views.questionFurtherMaths), #the url pointing to views.questionFurtherMaths which returns the question page if a user is practising further maths
    path('graph/', views.graph, name='graph'), #url pointing views.graph which returns the graphing calculator
    path('assessments/', views.assessment, name='assessment'), #url pointing to views.assessment which returns the weekly assessments page
    path('mathsSubject/', topics.views.mathsSubject, name='maths'), #url pointing to topic.views.subject which returns a page containing links to the maths topic pages
    path('fmathsSubject/', topics.views.furtherMathsSubject, name='furtherMaths'), #url pointing to topic.views.subject which returns a page containing links to the further maths topic pages
]