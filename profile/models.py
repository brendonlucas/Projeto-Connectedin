from django.db import models
from authentication.models import User


class Invite(models.Model):
    STATUS_INVITE_CHOICES=(
        ('0','waiting'),
        ('1','acepted'),
        ('2','refused')
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senders')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipients')
    status = models.CharField(max_length=2,choices=STATUS_INVITE_CHOICES,default='0')
    sended_at = models.DateField(auto_now_add=True, auto_now=False)

    def accept(self):
        Friendship(user=self.recipient,friend=self.sender).save()
        self.status = 1

    def reject(self):
        self.status = 2


class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend'),
    blocked=models.BooleanField(default=False)
    stated_at = models.DateField(auto_now_add=True, auto_now=False)

