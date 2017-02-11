from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect, get_object_or_404
from django.views import generic
from django.views.generic import ListView ,UpdateView

from forms import category_form
from forms import post_form
from main.models import post
from main.models import word_list, category
from . import forms

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)

def admindashboard(request):
    if request.user.is_superuser:
        return render(request, 'adminpanel/Base/fixed_sidebar.html')
    else:
        return redirect('/accounts/login/')


# add post
def add_post(request):
    if request.user.is_superuser:
        form = post_form()
        if request.method == 'POST':
            form = post_form(request.POST, request.FILES)
            if form.is_valid():
                form.post_img = request.FILES['post_img']
                form.save()
                return HttpResponseRedirect('/adminpanel/posts')

        context = {'post_form': form}
        return render(request, 'adminpanel/posts/post_form.html', context)
    else:
        return redirect('/accounts/login/')


class registerUser(SuperuserRequiredMixin,generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"


def allUsers(request):
    if request.user.is_superuser:
        allusers = User.objects.all()
        context = {'usersData': allusers}
        return render(request, 'adminpanel/users/allusers.html', context)
    else:
        return redirect('/accounts/login/')


def forbiddenWordsList(request):
    if request.user.is_superuser:
        wordlist= word_list.objects.all()
        return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )
    else:
        return redirect('/accounts/login/')

# show all posts
def show_all_posts(request):
    if request.user.is_superuser:
        all_posts = post.objects.all()
        context  = {'all_posts': all_posts}
        return render(request,'adminpanel/posts/index.html',context)
    else:
        return redirect('/accounts/login/')

#show post details
def post_details(request, post_id):
    if request.user.is_superuser:
        post_d = post.objects.get(id=post_id)
        context = {'post_d': post_d}
        return render(request, 'adminpanel/posts/post_details.html',context )
    else:
        return redirect('/accounts/login/')

# Edit Post
def edit_post(request, post_id):
    if request.user.is_superuser:
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
    else:
        return redirect('/accounts/login/')

# Delete Post
def delete_post(request, post_id):
    if request.user.is_superuser:
        post_d = post.objects.get(id=post_id)
        post_d.delete()
        return HttpResponseRedirect('/adminpanel/posts')
    else:
        return redirect('/accounts/login/')
#from braces import views
# Create your views here.


#def allUsers(request):
#    allusers = User.objects.all()
#    context = {'usersData': allusers}
#   return render(request, 'adminpanel/users/allusers.html', context)
#class allUsers(SuperuserRequiredMixin,models.Model):
#    model = User
#    template_name = "#..."
#    paginate_by = "#..."
class allUsers(SuperuserRequiredMixin,ListView):
    model = User
    template_name = "adminpanel/users/allusers.html"
    context_object_name = 'users_data'


def userProfile(request , user_id):
    if request.user.is_superuser:
        userData = User.objects.get(id=user_id)
        context = {'userData':userData}
        return render(request , 'adminpanel/users/userProfile.html' , context)
    else:
        return redirect('/accounts/login/')


class updateUser(SuperuserRequiredMixin,UpdateView):
    model = User
    fields =['username','email','is_superuser','is_active']
    template_name = "adminpanel/users/edituser.html"
    success_url = reverse_lazy('adminpanel:allusers')

    def get_obj(self, **kwargs):
        user_id = self.kwargs['pk']
        obj = User.objects.filter(pk=user_id)
        if obj.id != self.request.user.id and self.request.user.is_superuser:
            return HttpResponseRedirect('/adminpanel/users')
        return obj


   # def get_queryset(self):
   #     return reverse_lazy('allusers',kwargs={'pk': self.get_object().id})


def deleteUser(request, user_id):
    if request.user.is_superuser:
        user = User.objects.get(id=user_id)
        if user.is_superuser:
            return HttpResponseRedirect('/adminpanel/users')
        user.delete()
        return HttpResponseRedirect('/adminpanel/users')
    else:
        return redirect('/accounts/login/')

def blockUser(request, user_id):
    if request.user.is_superuser:
        user = User.objects.get(id = user_id)
        if user.is_superuser:
            return HttpResponseRedirect('/adminpanel/users')
        user.is_active = False
        user.save()
        return HttpResponseRedirect('/adminpanel/users')
    else:
        return redirect('/accounts/login/')

def unblockUser(request, user_id):
    if request.user.is_superuser:
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        return HttpResponseRedirect('/adminpanel/users')
    else:
        return redirect('/accounts/login/')

def forbiddenWordsList(request):
    if request.user.is_superuser:
        wordlist= word_list.objects.all()
        return render(request, 'adminpanel/forbiddenwords/index.html', {'wordlist': wordlist} )
    else:
        return redirect('/accounts/login/')

class ForbiddenWord_delete(SuperuserRequiredMixin,generic.DeleteView):
    model = word_list
    success_url = reverse_lazy('adminpanel:listWords')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



class ForbiddenWord_create(SuperuserRequiredMixin,generic.CreateView):
    form_class = forms.Forbidden_words_form
    success_url = reverse_lazy('adminpanel:listWords')
    template_name = "adminpanel/forbiddenwords/new.html"



class ForbiddenWord_edit(SuperuserRequiredMixin,generic.UpdateView):
    model = word_list
    fields = ["word_list"]
    template_name = "adminpanel/forbiddenwords/new.html"
    success_url = reverse_lazy('adminpanel:listWords')



def feature_post(request, post_id):
    if request.user.is_superuser:
        print "check admin"
        post_f = get_object_or_404(post, id = post_id)
        post_f.feature_status = True
        post_f.save()
        return HttpResponseRedirect('/adminpanel/posts')
    else:
        return redirect('/accounts/login/')

def unfeature_post(request, post_id):
    if request.user.is_superuser:
        post_f = get_object_or_404(post, id = post_id)
        post_f.feature_status = False
        post_f.save()
        return HttpResponseRedirect('/adminpanel/posts')
    else:
        return redirect('/accounts/login/')

#show category
def showCategory(request):
    if request.user.is_superuser:
        allCategory = category.objects.all()
        context = {'allCategory': allCategory}
        return render(request, 'adminpanel/category/index.html', context)
    else:
        return redirect('/accounts/login/')


# category details
def category_posts(request,id):
    if request.user.is_superuser:
        cat_post = post.objects.filter(post_cat_id_id=id)
        context = {'catposts':cat_post}
        return render (request , 'adminpanel/category/catposts.html' , context)
        #return HttpResponseRedirect('/adminpanel/category')
    else:
        return redirect('/accounts/login/')

# add category
def add_category(request):
    if request.user.is_superuser:
        form = category_form()
        if request.method == 'POST':
            form = category_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/adminpanel/category')

        context = {'category_form': form}
        return render(request, 'adminpanel/category/category_form.html', context)
    else:
        return redirect('/accounts/login/')

# edit category
def edit_category(request, id):
    if request.user.is_superuser:
        cat = category.objects.get(id=id)
        form = category_form(instance=cat)
        if request.method == 'POST':
            form = category_form(request.POST, instance=cat)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/adminpanel/category')

        context = {'category_form': form}
        return render(request, 'adminpanel/category/category_form.html', context)
    else:
        return redirect('/accounts/login/')

# delete category
def del_category(request, id):
    if request.user.is_superuser:
        cat = category.objects.get(id=id)
        cat.delete()
        return HttpResponseRedirect('/adminpanel/category')
    else:
        return redirect('/accounts/login/')