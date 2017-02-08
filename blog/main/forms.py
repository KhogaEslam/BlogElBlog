from django import forms
from models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('comment_body',)
        #exclude = ['comment_user_id','reply_comment_id','comment_post_id',]
