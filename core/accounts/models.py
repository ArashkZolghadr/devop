from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    description = models.TextField()
    
    
    def __str__(self):
        return self.author.username

    def get_avatar(self):
        """متد برای بازگرداندن عکس پروفایل"""
        if self.image:
            return self.image.url
        return '/static/img/default-avatar.jpg'