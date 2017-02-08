from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from main.models import word_list

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]
    def __init__(self, *args , **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["email"].label = "Email Address"

class Forbidden_words_form(forms.ModelForm):
	class Meta:
		model = word_list
		fields = ('word_list',)
