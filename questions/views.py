from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm


@login_required
def questions(request):
    """
    A view to add a question
    """
    question = Question.objects.all().order_by('-created_on')
    question_form = QuestionForm(request.POST)
    if request.method == 'POST':
        if question_form.is_valid():
            Question.objects.create(
                    user=request.user,
                    question_categories=request.POST['question_categories'],
                    question_comment=request.POST['question_comment'],
                )
            messages.success(request, 'Thank you for your question!')
        else:
            messages.error(request, 'Something went wrong')
            return redirect(reverse('questions'))

    template = 'questions/questions.html'
    context = {
        'question_form': question_form,
        'question': question,
    }

    return render(request, template, context)
