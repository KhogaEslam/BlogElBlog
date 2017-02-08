from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
<<<<<<< HEAD
from django import forms
from main.models import word_list
=======
from main.models import category
from django import forms
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]
    def __init__(self, *args , **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["email"].label = "Email Address"

<<<<<<< HEAD
class Forbidden_words_form(forms.ModelForm):
	class Meta:
		model = word_list
		fields = ('word_list',)
=======

class category_form(forms.ModelForm):
    class Meta:
        model = category
        fields = ['cat_title',]        
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
