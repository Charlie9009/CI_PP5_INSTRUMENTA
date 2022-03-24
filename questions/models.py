from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    The class for the question model
    """
    QUESTION_CHOICES = [
        (1, 'Products'),
        (2, 'Website'),
        (3, 'Profile'),
        (4, 'Delivery'),
        (5, 'Checkout'),
    ]
    user = models.ForeignKey(
        User,
        models.CASCADE
    )
    question_categories = models.IntegerField(
        default=0,
        choices=QUESTION_CHOICES
    )
    question_comment = models.TextField(
        max_length=240
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns the comment
        """
        return f'Question {self.question_comment} by {self.user}'
