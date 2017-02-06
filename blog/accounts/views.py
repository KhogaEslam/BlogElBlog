from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.contrib.auth.views import login
from django.http.response import HttpResponseRedirect

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home")
    else:
        return login(request)
# class LoginView(generic.FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy("/admin")
#     template_name = "accounts/login.html"
#     #def get_form(self, form_class=None):
#     #    if form_class is None :
#     #        form_class=self.get_form_class()
#     #    return form_class(self.request, **self.get_form_kwargs)
#     def form_valid(self, form):
#         login(self.request, form.get_user() )
#         return super().form_valid(form)
class RegisterView(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"
