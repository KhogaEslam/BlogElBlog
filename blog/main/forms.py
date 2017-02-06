from django import forms

from models import post, comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        exclude = ['post']
