from django.contrib import admin
from .models import BlogPost, Comment, Profile
from django.utils.translation import ngettext
from django.contrib import messages

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
    list_display = ('title', 'slug', 'status', 'published_date', 'isLiked')
    list_filter = ('status', )
    search_fields = ['title', 'text']
    prepopulated_fields = { 'slug' : ('title',)}
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Profile)