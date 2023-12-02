from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  """Returns the Home Page of this website"""
  return render(request, 'home/homepage.html')

def login(request):
  """Returns the Login Page"""
  return render(request, 'home/login.html')


def signup(request):
  """Returns the Sign Up Page"""
  return render(request, 'home/signup.html')