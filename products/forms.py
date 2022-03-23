from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review
from django.forms import RadioSelect


class ProductForm(forms.ModelForm):
    """
    Class for productform
    """
    class Meta:
        """
        Class for rendering the productform
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Update the fields in the form
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    A class the review form
    """
    class Meta:
        """
        Class for rendering rating and comments
        """
        model = Review
        fields = ('rating', 'comment',)

        widgets = {
            'rating': forms.RadioSelect(),
        }
