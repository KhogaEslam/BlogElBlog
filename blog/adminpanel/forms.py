from django import forms
from main.models import category

class category_form(forms.ModelForm):
    class Meta:
        model = category
        fields = ['cat_title',]
