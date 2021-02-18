from django.shortcuts import get_object_or_404, render
from .models import BlogPost
from .forms import CommentForm
from django.views import generic

# Create your views here.

class BlogPostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-published_date')
    template_name = 'blog_site_app/homepage.html'

# Render the single post detail
class BlogPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blog_site_app/post_detail.html'


def blogpost_detail(request, slug):
    template_name = 'blog_site_app/post_detail.html'
    blog_post = get_object_or_404(BlogPost, slug = slug)
    comments = blog_post.comments.filter(active=True)
    new_comment = None

    # Every comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        
        if comment_form.is_valid():
            # Create comment object but don't save to database
            new_comment = comment_form.save(commit=False)

            # Assign the current post to the comment
            new_comment.blog_post = blog_post

            # Save to database
            new_comment.save()
    else:
        comment_form  = CommentForm()

    return render(request, template_name, {
            'blog_post' : blog_post,
            'comments' : comments,
            'new_comment' : new_comment,
            'comment_form': comment_form })