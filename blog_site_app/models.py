from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image_avatar = models.ImageField(upload_to="images/")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()        
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    published_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    blog_image_post = models.ImageField(default="default_blog_image.jpg")
    active = models.BooleanField(default=False) # for the admin role to give confirmation
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

