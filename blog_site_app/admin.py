from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'published_date')
    list_filter = ('status', )
    search_fields = ['title', 'text']
    prepopulated_fields = { 'slug' : ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)