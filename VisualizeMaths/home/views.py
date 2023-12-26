from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SignupForm
from .models import StudentUser

# Create your views here.

def home(request):
  """Returns the Home Page of this website"""
  return render(request, 'home/homepage.html')

def login(request):
  """Returns the Login Page"""
  return render(request, 'home/login.html')

def checkMaths(value):
   """Checks that the maths field has been ticked."""
   str = "Username, Password and Maths are required fields."
   if value == "unknown" or value == "false":
      return str
   else:
      return True
   
def checkUsernameLength(value):
   """Checks if the username input is six characters long"""
   str = "Your Username must be at least six characters long."
   length = len(value)

   if length < 6:
      return str
   else:
      return True
   
def checkUsernameUnique(value):
   """Checks if the username input exists already."""
   str = "This username already exists."

   if StudentUser.objects.filter(username=value):
      return str
   else:
      return True
   
# The next four functions are for the password input   
def checkPasswordLength(value):
   """Checks that the password is at least 8 characters long."""
   str = "Your password should be at least 8 characters long, contain one number and one special character."
   length = len(value)

   if length < 8:
      return str
   else:
      return True

def checkForNumbers(value):
   """Checks that the password contains at least one number."""
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   str = "Your password should contain one number and one special character."

   if not any(i in numbers for i in value):
      return str
   else:
      return True
   
def checkCharacters(value):
   """Checks that the password contains at least one special character"""
   characters = ['`', '~', '!',  '@', '#',  '£', '$', '%', '^', '*', '(', ')', '{', '}', '[', ']', '-', '_', '+', '=', '|', '<', '>', ',', '.', '?', ':']
   str = "Your password should contain one special character."
   if not any(i in characters for i in value):
      return str
   else:
      return True

def signup(request):
  """Returns the Sign Up Page"""
  form = SignupForm()
  if request.method == 'POST':
        username = request.POST['username']
        passsword = request.POST['password']
        maths = request.POST['maths']
        test_one = checkMaths(maths)
        test_two = checkUsernameLength(username)
        test_three = checkUsernameUnique(username)
        test_four = checkPasswordLength(passsword)
        test_five = checkForNumbers(passsword)
        test_six = checkCharacters(passsword)

        #Checks the username length and the password length
        if test_two != True and test_four != True:
           context = {
              'test_two': test_two,
              'test_four': test_four,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
        #Checks that the maths field is required
        if test_one != True:
           context = {
              'test_one': test_one,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
        #Checks that the username is six characters long        
        if test_two != True:
           context = {
              'test_two': test_two,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
        #checks the password length
        if test_four != True:
           context = {
              'test_four': test_four,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        

        #checks if the username is unique
        if test_three != True:
           context = {
              'test_three': test_three,
              'form': form
           }
           return render(request, 'home/signup.html', context)

        #checks if the password contains at least one number
        if test_five != True:
           context = {
              'test_five': test_five,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
        #checks the password contains special characters
        if test_six != True:
           context = {
              'test_six': test_six,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
        #Last few tests before the user input is passed to the StudentUser table
        if (test_one, test_two, test_three, test_four, test_five, test_six) == True:
           form = SignupForm(request.POST)
           new_user = form.save(commit=False)
           new_user.save()
           success = "Student Account created successfully!"
           context = {
              'success': success,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        else:
           error = "You didn't fit the requirements below:"
           context = {
              'error': error,
              'form': form
           }
           return render(request, 'home/signup.html', context)
        
  context = {
    'form': form,
  }
  return render(request, 'home/signup.html', context)