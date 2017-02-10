from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     if username and password:
    #         print username, password
    #         user = authenticate(username=username, password=password)
    #         print user
    #         if  not user:
    #             raise forms.ValidationError("User does not exist.")
    #
    #     return super(LoginForm, self).clean(*args, **kwargs)
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]
    def __init__(self, *args , **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["email"].label = "Email Address"
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
