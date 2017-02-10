from django.shortcuts import render , HttpResponseRedirect, HttpResponse, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from forms import RegisterForm , EditForm
from main.models import word_list, category
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView ,UpdateView
from django.views.generic import TemplateView

from forms import category_form

from main.models import post
# Create your views here.
from forms import post_form

def checkAdmin(request):
#    print "super user ?", request.user.is_superuser
    if not request.user.is_superuser:
        return redirect('/accounts/login/')


def admindashboard(request):
    checkAdmin(request)
    if request.user.is_superuser:
        return render(request, 'adminpanel/Base/fixed_sidebar.html')
    else:
        return redirect('/accounts/login/')

# add post
def add_post(request):
    checkAdmin(request)
    form = post_form()
    if request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            form.post_img = request.FILES['post_img']
            form.save()
            return HttpResponseRedirect('/adminpanel/posts')

    context = {'post_form': form}
    return render(request, 'adminpanel/posts/post_form.html',context)

class registerUser(generic.CreateView):
#    def dispatch(self, request, *args, **kwargs):
#        if checkAdmin(request):
#            print "Hello!"
#            return super(allUsers, self).dispatch(request, *args, **kwargs)  # Don't forget this
#        else:
#            return redirect('/accounts/login/')
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"

def allUsers(request):
    checkAdmin(request)
    allusers = User.objects.all()
    context = {'usersData': allusers}
    return render(request, 'adminpanel/users/allusers.html', context)

def forbiddenWordsList(request):
    checkAdmin(request)
    wordlist= word_list.objects.all()
    return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )




# show all posts
def show_all_posts(request):
    checkAdmin(request)
    all_posts = post.objects.all()
    context  = {'all_posts': all_posts}
    return render(request,'adminpanel/posts/index.html',context)

#show post details
def post_details(request, post_id):
    checkAdmin(request)
    post_d = post.objects.get(id=post_id)
    context = {'post_d': post_d}
    return render(request, 'adminpanel/posts/post_details.html',context )

# Edit Post
def edit_post(request, post_id):
    checkAdmin(request)
    post_d = post.objects.get(id=post_id)
    form   = post_form(instance = post_d)
    if request.method == 'POST':
        form = post_form(request.POST,request.FILES, instance=post_d)
        if form.is_valid():
            #form.post_img = request.FILES['post_img']
            form.save()
            return HttpResponseRedirect('/adminpanel/posts')

    context = {'post_form': form}
    return render(request, 'adminpanel/posts/post_form.html',context)

# Delete Post
def delete_post(request, post_id):
    checkAdmin(request)
    post_d = post.objects.get(id=post_id)
    post_d.delete()
    return HttpResponseRedirect('/adminpanel/posts')
#from braces import views
# Create your views here.


#def allUsers(request):
#    allusers = User.objects.all()
#    context = {'usersData': allusers}
#   return render(request, 'adminpanel/users/allusers.html', context)
#class allUsers(models.Model):
#    model = User
#    template_name = "#..."
#    paginate_by = "#..."
class allUsers(ListView):
    model = User
    template_name = "adminpanel/users/allusers.html"
    context_object_name = 'users_data'

def userProfile (request , user_id):
    checkAdmin(request)
    userData = User.objects.get(id=user_id)
    context = {'userData':userData}
    return render(request , 'adminpanel/users/userProfile.html' , context)

from django.views.generic.detail import DetailView
from django.utils import timezone





class updateUser(UpdateView):
#    def dispatch(self, request, *args, **kwargs):
#        if checkAdmin(request):
#            print "Hello!"
#            return super(allUsers, self).dispatch(request, *args, **kwargs)  # Don't forget this
#        else:
#            return redirect('/accounts/login/')
    model = User
    fields =['username','email','is_superuser','is_active']
    template_name = "adminpanel/users/edituser.html"
    success_url = reverse_lazy('adminpanel:allusers')

    def get_obj(self, **kwargs):
        user_id = self.kwargs['pk']
        obj = User.objects.filter(pk=user_id)
        return obj

   # def get_queryset(self):
   #     return reverse_lazy('allusers',kwargs={'pk': self.get_object().id})


def deleteUser(request, user_id):
    checkAdmin(request)
    user = User.objects.get(id=user_id)
    user.delete()

    return HttpResponseRedirect('/adminpanel/users')

def blockUser(request, user_id):
    checkAdmin(request)
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect('/adminpanel/users')

def unblockUser(request, user_id):
    checkAdmin(request)
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/adminpanel/users')

def forbiddenWordsList(request):
    checkAdmin(request)
    wordlist= word_list.objects.all()
    return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )

class ForbiddenWord_delete(generic.DeleteView):
#    def dispatch(self, request, *args, **kwargs):
#        if checkAdmin(request):
#            print "Hello!"
#            return super(allUsers, self).dispatch(request, *args, **kwargs)  # Don't forget this
#        else:
#            return redirect('/accounts/login/')
    model = word_list
    success_url = reverse_lazy('adminpanel:listWords')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ForbiddenWord_create(generic.CreateView):
#    def dispatch(self, request, *args, **kwargs):
#        if checkAdmin(request):
#            print "Hello!"
#            return super(allUsers, self).dispatch(request, *args, **kwargs)  # Don't forget this
#        else:
#            return redirect('/accounts/login/')
    form_class = forms.Forbidden_words_form
    success_url = reverse_lazy('adminpanel:listWords')
    template_name = "adminpanel/forbiddenwords/new.html"

class ForbiddenWord_edit(generic.UpdateView):
#    def dispatch(self, request, *args, **kwargs):
#        if checkAdmin(request):
#            print "Hello!"
#            return super(allUsers, self).dispatch(request, *args, **kwargs)  # Don't forget this
#        else:
#            return redirect('/accounts/login/')
    model = word_list
    fields = ["word_list"]
    template_name = "adminpanel/forbiddenwords/new.html"
    success_url = reverse_lazy('adminpanel:listWords')

def feature_post(request, post_id):
    checkAdmin(request)
    print "check admin"
    post_f = get_object_or_404(post, id = post_id)
    post_f.feature_status = True
    post_f.save()
    return HttpResponseRedirect('/adminpanel/posts')

def unfeature_post(request, post_id):
    checkAdmin(request)
    post_f = get_object_or_404(post, id = post_id)
    post_f.feature_status = False
    post_f.save()
    return HttpResponseRedirect('/adminpanel/posts')

#show category
def showCategory(request):
    checkAdmin(request)
    allCategory = category.objects.all()
    context = {'allCategory': allCategory}
    return render(request, 'adminpanel/category/index.html', context)



# category details
def category_posts(request,id):
    cat_post = post.objects.filter(post_cat_id_id=id)
    context = {'catposts':cat_post}
    return render (request , 'adminpanel/category/catposts.html' , context)
    #return HttpResponseRedirect('/adminpanel/category')


# add category
def add_category(request):
    checkAdmin(request)
    form = category_form()
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/category')

    context = {'category_form': form}
    return render(request, 'adminpanel/category/category_form.html', context)


# edit category
def edit_category(request, id):
    checkAdmin(request)
    cat = category.objects.get(id=id)
    form = category_form(instance=cat)
    if request.method == 'POST':
        form = category_form(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpanel/category')

    context = {'category_form': form}
    return render(request, 'adminpanel/category/category_form.html', context)
# delete category
def del_category(request, id):
    checkAdmin(request)
    cat = category.objects.get(id=id)
    cat.delete()
    return HttpResponseRedirect('/adminpanel/category')
