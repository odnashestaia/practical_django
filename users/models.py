from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    friends = models.ManyToManyField(User, related_name='my_friends', blank=True)
    bio = models.CharField(max_length=250, blank=True)
    data_of_birt = models.DateField()