from django.db import models
from django.contrib.auth.models import User

from products.models import Product



class Wishlist(models.Model):
    """
    A model for a users wishlist
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        Product,
        blank=True
    )

    def __str__(self):
        """
        Return user wishlist
        """
        return f"{self.user}'s wishlist"
