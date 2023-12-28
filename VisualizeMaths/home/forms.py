from .models import StudentUser
from django import forms

class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=250, widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'sign-up-field'

    class Meta:
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
        #defines the fields from StudentUser that is shown on the login page
        model = StudentUser
        fields = ["username", "password",]
        labels = {
            "username": "Username",
            "password": "Password",
        }