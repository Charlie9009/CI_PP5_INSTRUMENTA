from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    The class for the category model
    """
    class Meta:
        """
        Change spelling on admin page
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the category name
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """
    The class for the products model
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(
        max_length=254
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns the product name
        """
        return self.name


class Review(models.Model):
    """
    The class for the review model
    """
    RATING_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(
        User,
        models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        models.CASCADE
    )
    comment = models.TextField(
        max_length=240
    )
    rating = models.IntegerField(
        default=0,
        choices=RATING_CHOICE
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns the comment
        """
        return self.comment
