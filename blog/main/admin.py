from django.contrib import admin

# Register your models here.
from .models import post, category, comment, word_list

class post_custom(admin.StackedInline):
    model = post
    extra = 2

class post_custom_2(admin.ModelAdmin):
    list_display = ('post_title', 'post_content', 'post_img', 'post_cat_id')
    fieldsets = (
        	['Post Content', {'fields':['post_title', 'post_content']}],
    		['Post Image',{'fields':['post_img']} ],
            ['Post Category',{'fields':['post_cat_id']} ]
    )


class category_custom(admin.ModelAdmin):
    inlines = [post_custom]

admin.site.register(post,post_custom_2)
admin.site.register(category,category_custom)
admin.site.register(comment)
admin.site.register(word_list)
