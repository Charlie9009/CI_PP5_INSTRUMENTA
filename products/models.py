from django.db import models


class Category(models.Model):
    """
    The class for the category model
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

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
