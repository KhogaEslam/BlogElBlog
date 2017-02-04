from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Categories table
class category(models.Model):
    cat_title =models.CharField(max_length= 200)

#Posts table
class post(models.Model):

    post_title = models.CharField(max_length = 200)
    post_content = models.TextField()
    post_img=models.ImageField(upload_to="./media/", blank=True)
    post_date=models.DateField(auto_now_add = True)
    post_cat_id=models.ForeignKey(category)

#Comments table
class comment(models.Model):
    comment_body = models.TextField()
    comment_date=models.DateField(auto_now_add = True)
    comment_user_id=models.ForeignKey(User)
    reply_comment_id = models.ForeignKey("comment")
    comment_post_id = models.ForeignKey(post)

# Words list table
class word_list(models.Model):
    word_list = models.CharField(max_length=50)
