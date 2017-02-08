from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from main.models import post
from forms import post_form

def admindashboard(request):
	return render(request, 'adminpanel/admin.html')
# add post
def add_post(request):
	form = post_form()
	if request.method == 'POST':
		form = post_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/adminpanel/posts')

	context = {'post_form': form}
	return render(request, 'adminpanel/posts/post_form.html',context)

# show all posts
def show_all_posts(request):
    all_posts = post.objects.all()
    context  = {'all_posts': all_posts}
    return render(request,'adminpanel/posts/index.html',context)

#show post details
def post_details(request, post_id):
	post_d = post.objects.get(id=post_id)
	context = {'post_d': post_d}
	return render(request, 'adminpanel/posts/post_details.html',context )

# Edit Post
def edit_post(request, post_id):
    post_d = post.objects.get(id=post_id)
    form   = post_form(instance = post_d)
    if request.method == 'POST':
        form = post_form(request.POST, instance=post_d)
        if form.is_valid():
			form.save()
			return HttpResponseRedirect('/adminpanel/posts')

    context = {'post_form': form}
    return render(request, 'adminpanel/posts/post_form.html',context)

# Delete Post
def delete_post(request, post_id):
	post_d = post.objects.get(id=post_id)
	post_d.delete()
	return HttpResponseRedirect('/adminpanel/posts')
