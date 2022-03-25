from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """
    A class for the question form
    """
    class Meta:
        """
        Class for rendering question form
        """
        model = Question
        fields = ('question_categories', 'question_comment',)

