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