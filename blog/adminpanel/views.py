from django.shortcuts import render , HttpResponseRedirect
from django.views import generic
from forms import RegisterForm , EditForm
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from main.models import word_list, category
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.db import models
from django.contrib.auth.models import User

from forms import category_form

# Create your views here.

class registerUser(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"

def forbiddenWordsList(request):
    wordlist= word_list.objects.all()
    return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )



# Create your views here.
def showCategory(request):
    allCategory = category.objects.all()
    context = {'allCategory': allCategory}
    return render(request, 'adminpanel/category/index.html', context)


# add
def add_category(request):
    form = category_form()
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanal/all')

    context = {'cat_form': form}
    return render(request, 'adminpanel/category_form.html', context)


class allUsers(ListView):
    model = User
    template_name = "adminpanel/users/allusers.html"
    context_object_name = 'users_data'

def userProfile (request , user_id):
    userData = User.objects.get(id=user_id)
    context = {'userData':userData}
    return render(request , 'adminpanel/users/userProfile.html' , context)

from django.views.generic.detail import DetailView
from django.utils import timezone


# edit
def edit_category(request, id):
    cat = category.objects.get(id=id)
    form = category_form(instance=cat)
    if request.method == 'POST':
        form = category_form(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/all')

    context = {'cat_form': form}
    return render(request, 'adminpanel/category_form.html', context)


# delete
def del_category(request, id):
    cat = category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/adminpanel/all')


class updateUser(UpdateView):
    model = User
    fields =['is_superuser','is_active']
    template_name = "adminpanel/users/edituser.html"
    success_url = reverse_lazy('adminpanel:allusers')

    def get_obj(self, **kwargs):
        user_id = self.kwargs['pk']
        obj = User.objects.filter(pk=user_id)
        return obj



def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()

    return HttpResponseRedirect('/adminpanel/users/all')

def blockUser(request, user_id):
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect('/adminpanel/users/all')

def unblockUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/adminpanel/users/all')