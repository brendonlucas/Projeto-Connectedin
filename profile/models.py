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
        self.sender.friendship.add(self.recipient)
        self.recipient.friendship.add(self.sender)
        self.status = 1

    def reject(self):
        self.status = 2


