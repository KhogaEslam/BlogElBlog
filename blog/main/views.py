from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth


# Create your views here.
from django.http import HttpResponseRedirect
from models import post , comment , word_list, category

def homePosts (request):
    posts = post.objects.all().order_by('-post_date')
    categories = category.objects.all()
    paginator = Paginator(posts , 1 )
    page = request.GET.get('page')
    try:
        posts_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts_data = paginator.page(paginator.num_pages)
    current_user = request.user
    subscribed_cats = category.objects.filter(user = current_user.id)
    context = {'posts': posts_data , 'categories': categories, "subscribedCats": subscribed_cats }
    return render(request , 'main/home.html' , context)

def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    return HttpResponseRedirect('/home')
def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/home')

def modelSelect(request, model_name):
    if (model_name == "category" or model_name == "post" or model_name == "word_list" or model_name == "User"):
        objs = eval(model_name).objects.all()
        return render(request, 'main/list.html', {"objs", objs})
    else:
        return HttpResponseRedirect("/admin")
