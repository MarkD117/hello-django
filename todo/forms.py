from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # inner class provides the form some information about itself
    # like what fields it should render and how it should display
    # error messages and so on.
    class Meta:
        model = Item
        fields = ['name', 'done']
