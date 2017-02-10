from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.contrib.auth.views import login
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist

def my_login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form = forms.LoginForm()
        errMsg = ""
        form = forms.LoginForm(request.POST)
        print "Form", form
        if request.method == "POST":
            #print "Request method", request.method, "Form valid ? ", form.is_valid()
            if not form.is_valid() or form.is_valid():
                #print "Form valid1", form.is_valid()
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username, password=password)
                errMsg = ""
                #return None if user not authenticated
                #print "user is: ", user
                active = False
                is_user = False
                try:
                    user = User.objects.get(username=username)
                    is_user = True
                    #print "user object: ", user
                    #user exists
                except Exception:
                    #print "is_User: ", is_user
                    #user not found
                    errMsg += "<div class =\"alert alert-danger\" role=\"alert\" ><p>"+"User doesn't Exist!"+"</p></div>"

                    #print "errMsg1", errMsg
                    return render(request, "accounts/login.html", {'form': form, 'err':errMsg})
                else:
                    if not check_password(password, user.password):
                        #print "Password incorrect"
                        errMsg += "<div class =\"alert alert-danger\" role=\"alert\" ><p>" + "Check Your Password, and try again." + "</p></div>"
                        #print "errMsg2",errMsg
                        return render(request, "accounts/login.html", {'form': form, 'err':errMsg})
                    else:
                        active = user.is_active
                        #print "activ", active
                        if is_user and active:
                            #print user
                            #print user.is_active
                            login(request, user)
                            #print "errMsg3", errMsg
                            return HttpResponseRedirect('/home')
                        else:
                            errMsg += "<div class =\"alert alert-danger\" role=\"alert\" ><p>" + "You are blocked, contact the admin." + "</p></div>"
                            #print "errMsg3", errMsg
                            return render(request, "accounts/login.html", {'form': form, 'err':errMsg})
        return render(request, "accounts/login.html", {'form': form, 'err':errMsg})

# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout


#def custom_login(request):
#    if request.user.is_authenticated():
#        return HttpResponseRedirect("/home")
#    else:
#        return login(request)
#def custom_login(request):
#	error = {}
#	try:
#		username = request.Post['username']
#		password = request.Post['password']
#		user = authenticate(username=username, password=password)
#		if user is not None:
#			if user.is_active:
#				auth_login(request, user)
#			else:
#				error = 'Non active user'
#		else:
#			 error = 'Wrong username or password'
#	except:
#		 error  = ''
#
#	#populateContext(request, context)
#	return render(request, 'accounts/login.html', {'errorerror)

# class LoginView(generic.FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy("/admin")
#     template_name = "accounts/login.html"
#     def get_form(self, form_class=None):
#        if form_class is None :
#            form_class=self.get_form_class()
#        return form_class(self.request, **self.get_form_kwargs)
#     def form_valid(self, form):
#         login(self.request, form.get_user() )
#         return super().form_valid(form)
class RegisterView(generic.CreateView):
    form_class = forms.RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"
