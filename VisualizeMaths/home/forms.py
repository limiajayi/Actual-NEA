from .models import StudentUser #table that contains the student users imported from models.py
from django import forms #an inbuilt django class for html form handling

class SignupForm(forms.ModelForm):
    """Creates a form based on the StudentUser table"""
    password = forms.CharField(max_length=250, widget = forms.PasswordInput()) #hides the password while it's being typed in the form

    def __init__(self, *args, **kwargs):
        #when the form is being initialised this adds a class of sign-up-field to each input box
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'sign-up-field'

    class Meta:
        #an object that specifies which fields from a table should be added and makes sure they do not clash with extra fields defined in the form
        model = StudentUser
        fields = "__all__"
        labels = {
            "username": "Username",
            "password": "Password",
            "maths": "Maths",
            "further_maths": "Further Maths",
        }

class LoginForm(forms.ModelForm):
    """A form for users to login"""
    password = forms.CharField(max_length=250, widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        #Adds a class of login-field to form elements
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'login-field'
    
    class Meta:
        #an object that specifies which fields from a table should be added and makes sure they do not clash with extra fields defined in the form
        model = StudentUser
        fields = ["username", "password",]
        labels = {
            "username": "Username",
            "password": "Password",
        }