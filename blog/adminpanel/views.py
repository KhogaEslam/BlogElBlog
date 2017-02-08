from django.shortcuts import render , HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from forms import RegisterForm , EditForm
from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView ,UpdateView

# Create your views here.

class registerUser(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('adminpanel:adduser')
    template_name = "adminpanel/users/adduser.html"

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
    userData = User.objects.get(id=user_id)
    context = {'userData':userData}
    return render(request , 'adminpanel/users/userProfile.html' , context)

from django.views.generic.detail import DetailView
from django.utils import timezone



#    model = Article

 #   def get_context_data(self, **kwargs):
  #      context = super(ArticleDetailView, self).get_context_data(**kwargs)
   #     context['now'] = timezone.now()
#        return context

class updateUser(UpdateView):
    model = User
    fields =['is_superuser','is_active']
    template_name = "adminpanel/users/edituser.html"
    success_url = reverse_lazy('adminpanel:allusers')

    #def get(self, request, **kwargs):
        #self.object = User.objects.get(id=self.kwargs['pk'])
      #  context = self.get_context_data(object=self.object)
       # return self.render_to_response(context)

    def get_obj(self, **kwargs):
        user_id = self.kwargs['pk']
        obj = User.objects.filter(pk=user_id)
        return obj

   # def get_queryset(self):
   #     return reverse_lazy('allusers',kwargs={'pk': self.get_object().id})


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