from django.db import models

# Create your models here.


# authapp/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=30, default='offline')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
