from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  """Returns the Home Page of this website"""
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())