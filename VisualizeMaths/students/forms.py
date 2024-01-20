from django import forms
from .models import Question

NUM_CHOICES = [tuple([x,x]) for x in range(10, 45, 10)]

class QuestionForm(forms.ModelForm):
    number_of_questions = forms.IntegerField(widget=forms.Select(choices=NUM_CHOICES))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'qform-field'

    class Meta:
        model = Question
        fields = ["subject", "topic", "difficulty"]