from django.db import models
from django import forms
from myadminapp.models import blogdata

# Create your models here.

class Comment(models.Model):
    blog_post = models.ForeignKey(blogdata, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'subject', 'message']
