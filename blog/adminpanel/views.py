from django.shortcuts import render
from main.models import word_list, category , post
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.db import models
from django.contrib.auth.models import User

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



# Show Categories
def showCategory(request):
    allCategory = category.objects.all()
    context = {'allCategory': allCategory}
    return render(request, 'adminpanel/category/index.html', context)
# category details
def category_posts(request,id):
    cat_post = post.objects.filter(post_cat_id_id=id)
    context = {'catposts':cat_post}
    return render (request , 'adminpanel/category/catposts.html' , context)
    #return HttpResponseRedirect('/adminpanel/category')


# add
def add_category(request):
    form = category_form()
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/category')

    context = {'category_form': form}
    return render(request, 'adminpanel/category/category_form.html', context)


# edit
def edit_category(request, id):
    cat = category.objects.get(id=id)
    form = category_form(instance=cat)
    if request.method == 'POST':
        form = category_form(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/category')

    context = {'category_form': form}
    return render(request, 'adminpanel/category/category_form.html', context)

# delete
def del_category(request, id):
    cat = category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/adminpanel/category')
