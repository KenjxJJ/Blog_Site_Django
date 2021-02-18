from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    published_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title

