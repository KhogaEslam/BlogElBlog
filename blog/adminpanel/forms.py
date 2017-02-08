from django import forms
from main.models import post

class post_form(forms.ModelForm):
    class Meta:
        model  = post
        fields = ['post_title','post_content','post_img','post_cat_id']
