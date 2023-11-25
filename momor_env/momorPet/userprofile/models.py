from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(
        User, related_name='userprofile', on_delete=models.CASCADE)
    is_vendor = modls.BooleanField(default=False)

    def __str__(self):
        return self.user.username
