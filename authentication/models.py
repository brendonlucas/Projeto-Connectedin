from django.db import models
import secrets
import django.contrib.auth.models as adminModels

class User(adminModels.User):
  # USER_STATUS_CHOICES = (
  #   (0,'inactive'),
  #   (1,'active'),
  # )
  bio = models.CharField(max_length=180, blank=True)
  email_verified = models.DateField(auto_now=False, auto_now_add=False)
  verification_code=models.CharField(max_length=128,blank=False, db_index=True, unique=True)

  def save(self):
    token = secrets.token_hex(20)
    while len(User.objects.filter(verification_code=token)) > 0:
      token = secrets.token_hex(20)
    self.verification_code = token
    super(User, self).save()
    