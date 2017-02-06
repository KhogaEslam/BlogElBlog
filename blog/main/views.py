from django.shortcuts import render , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth


# Create your views here.
from django.http import HttpResponse
from models import post , comment , word_list,category

def homePosts (request):
    posts = post.objects.all().order_by('-post_date')
    cats = category.objects.all()

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

    context = {'posts': posts_data , 'cat': cats}
    return render(request , 'main/home.html' , context)

def PostDetails(request, id):
    #return HttpResponse('details of %s' %id)
    postDetails =  get_object_or_404(post, id = id)
    categoryDetails = postDetails.post_cat_id
    comments = comment.objects.filter(comment_post_id = postDetails.id)
    context = {'postDetails': postDetails, 'postCat': categoryDetails, 'comments': comments}
    return render(request, 'post/postDetails.html',context )
