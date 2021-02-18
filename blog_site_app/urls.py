from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostList.as_view(), name="home"),
    path('<slug:slug>/', views.blogpost_detail, name='post_detail'),
]
