from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.BlogPostList.as_view(), name="home"),
    path('create_account', views.create_account, name="create_account"),
    path('login', auth_views.LoginView.as_view(template_name = 'blog_site_app/login.html'), name="login"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('new', views.add_new_blog_post, name="new_blog_post"),
    path('like/<id>', views.like, name="like"),
    path('my-blogs', views.single_user_blog_posts, name="my_blog_posts"),
    path('edit/<slug:slug>', views.edit_blog_post, name="edit_blog_post"),
    path('<slug:slug>/remove/', views.blog_post_remove, name="blog_post_remove"),
    path('logout',auth_views.LogoutView.as_view(template_name = 'blog_site_app/homepage.html'), {'next_page': '/login'}, name="logout"),
    path('<slug:slug>/', views.blogpost_detail, name='post_detail')
]
