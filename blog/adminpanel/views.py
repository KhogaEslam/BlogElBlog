from django.shortcuts import render
<<<<<<< HEAD
from main.models import word_list
=======
from main.models import word_list, category
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.views.generic import TemplateView
=======

from django.http import HttpResponse, HttpResponseRedirect
from forms import category_form

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


>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc

from braces import views
# Create your views here.
<<<<<<< HEAD

class registerUser(generic.CreateView, views.SuperuserRequiredMixin):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"

class allUsers(generic.ListView):
    model = User
    template_name = "adminpanel/users/allusers.html"
    context_object_name = 'users_data'

def forbiddenWordsList(request):
    wordlist= word_list.objects.all()
    return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )

class ForbiddenWord_delete(generic.DeleteView):
    model = word_list
    success_url = reverse_lazy('adminpanel:listWords')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ForbiddenWord_create(generic.CreateView):
    form_class = forms.Forbidden_words_form
    success_url = reverse_lazy('adminpanel:listWords')
    template_name = "adminpanel/forbiddenwords/new.html"

class ForbiddenWord_edit(generic.UpdateView):
    model = word_list
    fields = ["word_list"]
    template_name = "adminpanel/forbiddenwords/new.html"
    success_url = reverse_lazy('adminpanel:listWords')

def userProfile (request , user_id):
    userData = User.objects.get(id=user_id)
    context = {'userData':userData}
    return render(request , 'adminpanel/users/userProfile.html' , context)

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
=======
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
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
