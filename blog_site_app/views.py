from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost
from .forms import CommentForm
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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

#  Create account page
def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=user_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog_site_app/create_account.html', {'form': form })

#  Login functionality
def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request,'blog_site_app/homepage.html', { 'user': user })        
    else:  
        if request.method == "POST":
            context = { 'message': 'Please login with right credentials' }
            return render(request, 'blog_site_app/login.html', context = context )       
        return render(request,'blog_site_app/login.html')
            

