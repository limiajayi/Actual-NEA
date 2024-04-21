from django import forms #an inbuilt django class for html form handling
from .models import Question #a table that contains questions

NUM_CHOICES = [tuple([x,x]) for x in range(10, 45, 10)] #lets users filter questions from 10 to 40, incrementing every ten values

class QuestionForm(forms.ModelForm):
    number_of_questions = forms.IntegerField(widget=forms.Select(choices=NUM_CHOICES)) #uses num-choices as a drop down menu to let users sort for the number of questions they want

    def __init__(self, *args, **kwargs):
        #initialises the form with a class of qform-field on each input element
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'qform-field'

    class Meta:
        #an object that specifies which fields from a table should be added and makes sure they do not clash with extra fields defined in the form, for example, number questions field above
        model = Question
        fields = ["subject", "topic", "difficulty", "exam_board"]