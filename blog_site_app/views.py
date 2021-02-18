from django.shortcuts import render
from .models import BlogPost
from django.views import generic

# Create your views here.

#  display the home page first
# def home_page(request):
#     return render(request,'blog_site_app/homepage.html')

class BlogPostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-published_date')
    template_name = 'blog_site_app/homepage.html'
