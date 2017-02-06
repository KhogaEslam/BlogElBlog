from django.contrib import admin

# Register your models here.
from .models import post, category, comment, word_list
admin.site.register(post)
admin.site.register(category)
admin.site.register(comment)
admin.site.register(word_list)
