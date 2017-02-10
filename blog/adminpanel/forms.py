from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.contrib.auth.models import User
from main.models import category, word_list
from django import forms
from main.models import post


class post_form(forms.ModelForm):
    class Meta:
        model = post
        fields = ['post_title', 'post_content', 'post_img', 'post_cat_id']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
#        self.fields["username"].label = "User Name"
#        self.fields["email"].label = "Email Address"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class Forbidden_words_form(forms.ModelForm):
	class Meta:
		model = word_list
		fields = ('word_list',)

class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields= ["username", "email"]
    def __init__(self, *args , **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["email"].label = "Email Address"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class category_form(forms.ModelForm):
    class Meta:
        model = category
        fields = ['cat_title',]
