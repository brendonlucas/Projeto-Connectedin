from django.db import models
from posts.models import Post


class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_report')
    comment = models.CharField(max_length=255, null=True)
    date_report = models.DateField()
    amount = models.IntegerField()
