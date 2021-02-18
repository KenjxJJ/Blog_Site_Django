from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog_post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'published_date')
    list_filter = ('status', )
    search_fields = ['title', 'text']
    prepopulated_fields = { 'slug' : ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)