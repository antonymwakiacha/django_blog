from django.db import models
from django.contrib.auth.models import User
from post.models import Post

from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(blank=True, max_length=150)
    created= models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)
    picture= models.ImageField(upload_to='profile_pictures',blank=True,null=True,verbose_name='Picture')

def create_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender =User)
post_save.connect(save_user_profile, sender =User)


    # def __str__(self):
    #     self.user