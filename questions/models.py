from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """
    The class for the question model
    """
    QUESTION_CHOICES = [
        ('Products', 'Products'),
        ('Website', 'Website'),
        ('Profile', 'Profile'),
        ('Delivery', 'Delivery'),
        ('Checkout', 'Checkout'),
    ]
    user = models.ForeignKey(
        User,
        models.CASCADE
    )
    question_categories = models.CharField(
        max_length=70,
        default='Products',
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
