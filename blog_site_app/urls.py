from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPostList.as_view(), name="home"),
    path('create_account/', views.create_account, name="create_account"),
    path('<slug:slug>/', views.blogpost_detail, name='post_detail')
]
