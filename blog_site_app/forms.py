from .models import BlogPost, Comment,Profile
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "location","birth_date", "image_avatar")


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "text","status",)
