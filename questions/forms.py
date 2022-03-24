from django import forms
from django.forms import RadioSelect
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
        fields = ('question_categories', 'question_comment',)

