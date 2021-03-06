from django.contrib.sites import requests
from django.shortcuts import render , render_to_response, redirect,  get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from forms import CommentForm
from models import post , comment , word_list ,category
from django.contrib.auth.models import User
import random
import re
# Create your views here.
class OffensiveWordsFilter(object):
    def __init__(self, filterlist, ignore_case=True, replacements="$@%-?!", complete=True, inside_words=False):
        self.badwords = filterlist
        self.ignore_case = ignore_case
        self.replacements = replacements
        self.complete = complete
        self.inside_words = inside_words

    def _make_clean_word(self, length):
        return ''.join([random.choice(self.replacements) for i in
                  range(length)])

    def __replacer(self, match):
        value = match.group()
        if self.complete:
            return self._make_clean_word(len(value))
        else:
            return value[0]+self._make_clean_word(len(value)-2)+value[-1]

    def clean(self, text):
        regexp_insidewords = {
            True: r'(%s)',
            False: r'\b(%s)\b',
            }

        regexp = (regexp_insidewords[self.inside_words] %
                  '|'.join(self.badwords))

        r = re.compile(regexp, re.IGNORECASE if self.ignore_case else 0)

        return r.sub(self.__replacer, text)

def wordsCleaner(sentence):
    badwords = word_list.objects.values_list('word_list', flat=True)
    if badwords.exists():
        owf = OffensiveWordsFilter(badwords, replacements="*")
        #print f.clean(sentence)
        owf.inside_words = True
        #print f.clean(sentence)
        owf.complete = False
        #print f.clean(sentence)
        return owf.clean(sentence)
    else:
        return sentence

def homePosts (request):
    posts = post.objects.all().order_by('-post_date')
    feature_posts = post.objects.filter(feature_status=True)[:5]
    categories = category.objects.all()

    paginator = Paginator(posts , 5 )
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
    context = {'posts': posts_data , 'feature_posts': feature_posts, 'categories': categories, "subscribedCats": subscribed_cats }
    return render(request , 'main/home.html' , context)

import smtplib

from email.mime.text import MIMEText

def confirmSubscription(current_user, Category):
    fName='Beloved'
    lName='Member'
    lambda fName: current_user.first_name if current_user.first_name != None else 'Beloved'
    lambda lName: current_user.last_name if current_user.last_name  != None else 'Member'
    textMsg = "Dear "+fName+" "+lName+" ("+current_user.username+"): you have subscribed to new category "
    msg = MIMEText(textMsg+Category)
    msg['Subject'] = "Hello"+current_user.first_name+" "+current_user.last_name+" ("+current_user.username+"), we heve news for you"
    msg['From'] = "khogaeslam@gmail.com"
    msg['To'] = current_user.email

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandboxa9f988908bd44b8892f62e305b8c7572.mailgun.org', '7edcbf92ebdd1f395dd01deee3d4d3f7')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    confirmSubscription(current_user,subscribed_cats.cat_title)
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

def PostDetails(request, id):
    #return HttpResponse('details of %s' %id)
    postDetails =  get_object_or_404(post, id = id)
    categoryDetails = postDetails.post_cat_id
    post_views_num  = postDetails.post_views + 1
    postDetails .post_views = post_views_num
    postDetails.save()
    #comments = comment.objects.filter(comment_post_id = postDetails.id)
    form = CommentForm(request.POST or None)

    context = {'postDetails': postDetails, 'postCat': categoryDetails, 'form': form}
    return render(request, 'post/postDetails.html', context )

def addComment(request, postID):
    print postID, request.user
    if request.method == 'POST':
	    comment = CommentForm(request.POST, request.FILES)
	    if comment.is_valid():
		    comment = comment.save(commit=False)
            comment.comment_body = wordsCleaner(comment.comment_body)
            comment.post = post.objects.get(id = postID)
            #comment.User = User.objects.get(id = request.user.id)
            comment.comment_user_id_id = request.user.id
            comment.comment_post_id_id = postID

            comment.save()
            return redirect(request.path)
    return HttpResponseRedirect("/main/"+postID+"/post")

def addReply(request, postID, commentID):
    if request.method == 'POST':
	    reply = CommentForm(request.POST, request.FILES)
	    if reply.is_valid():
		    reply = reply.save(commit=False)
            reply.comment_body = wordsCleaner(reply.comment_body)
            reply.post = post.objects.get(id = postID)
            #comment.User = User.objects.get(id = request.user.id)
            reply.comment_user_id_id = request.user.id
            reply.comment_post_id_id = postID
            reply.reply_comment_id = comment.objects.get(id = commentID)

            reply.save()
            return redirect(request.path)
    return HttpResponseRedirect("/main/"+postID+"/post")

def deleteComment(request, postID, commentID):
    comment.objects.filter(reply_comment_id=commentID).delete()
    comment.objects.filter(id=commentID).delete()
    return HttpResponseRedirect("/main/"+postID+"/post")

def category_posts(request,cat_id):
    cat_post = post.objects.filter(post_cat_id_id=cat_id)
    paginator = Paginator(cat_post , 5 )
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
    context = {'catposts':cat_post,'posts': posts_data  }

    return render (request , 'post/catPosts.html' , context)
