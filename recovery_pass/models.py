from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from authentication.models import User
from django.db import models


class Send(AbstractBaseUser, models.Model):
    body_link = models.CharField(max_length=255, null=True)
    date_link = models.DateField(auto_now=True)
    active = models.BooleanField(default=1)
    user_link = models.ForeignKey(User, on_delete=models.CASCADE, related_name='link_user')
