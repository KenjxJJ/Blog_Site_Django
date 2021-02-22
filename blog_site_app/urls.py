from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.BlogPostList.as_view(), name="home"),
    path('create_account', views.create_account, name="create_account"),
    path('login', auth_views.LoginView.as_view(template_name = 'blog_site_app/login.html'), name="login"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('logout',auth_views.LogoutView.as_view(template_name = 'blog_site_app/homepage.html'), {'next_page': '/login'}, name="logout"),
    path('<slug:slug>/', views.blogpost_detail, name='post_detail')
]
