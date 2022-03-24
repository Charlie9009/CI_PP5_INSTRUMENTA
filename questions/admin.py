from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    """
    Class for the product model
    """
    list_display = ('user', 'question_categories', 'question_comment',
                    'created_on',)
    list_filter = ('user', 'question_categories', 'question_comment', 'created_on',)
    search_fields = ('user', 'question_categories', 'question_comment', 'created_on',)


admin.site.register(Question, QuestionAdmin)
