from django.db import models
from django.contrib.auth.models import User
from post.models import Post

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50,null=True,blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(blank=True, max_length=150)
    created= models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)

    def __str__(self):
        self.user