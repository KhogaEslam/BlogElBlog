from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#Categories table
class category(models.Model):
    cat_title = models.CharField(max_length= 200)
    user = models.ManyToManyField(User, blank=True)

    def __str__ (self):
        return self.cat_title


#Posts table
class post(models.Model):

    post_title = models.CharField(max_length = 200)
    post_content = models.TextField()
    post_img=models.ImageField(upload_to="./static/media/", blank=True)
    post_date=models.DateField(auto_now_add = True)
    post_cat_id=models.ForeignKey(category)
    def __str__ (self):
        return self.post_title

    def __str__(self):
        return self.post_title

#Comments table
class comment(models.Model):
    comment_body = models.TextField()
    comment_date=models.DateField(auto_now_add = True)
    comment_user_id=models.ForeignKey(User)
    reply_comment_id = models.ForeignKey('self', null=True, blank=True)
    comment_post_id = models.ForeignKey(post)
    def __str__ (self):
        return self.comment_body

    def __str__(self):
        return self.comment_body

# Words list table
class word_list(models.Model):
    word_list = models.CharField(max_length=50)
<<<<<<< HEAD
    def __str__ (self):
        return self.word_list
=======

    def __str__(self):
        return self.word_list
#    cat_id = models.ForeignKey(category)
#    user_id = models.ForeignKey(User)
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
