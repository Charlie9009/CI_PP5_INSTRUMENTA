from django import forms
from django.forms import RadioSelect
from .widgets import CustomClearableFileInput
from .models import Question


class QuestionForm(forms.ModelForm):
    """
    A class for the question form
    """
    class Meta:
        """
        Class for rendering rating and comments
        """
        model = Question
        fields = ('question_category', 'comment',)

        widgets = {
            'rating': forms.RadioSelect(),
        }
