from django.shortcuts import render
from main.models import word_list
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.db import models
from django.contrib.auth.models import User

# Create your views here.

class registerUser(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"

def allUsers(request):
    allusers = User.objects.all()
    context = {'usersData': allusers}
    return render(request, 'adminpanel/users/allusers.html', context)
def forbiddenWordsList(request):
    wordlist= word_list.objects.all()
    return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )
