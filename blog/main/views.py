from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
from django.http import HttpResponse
from models import post , comment , word_list

def homePosts (request):
    posts = post.objects.all().order_by('-post_date')
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

    context = {'posts': posts_data }
    return render(request , 'main/home.html' , context)
