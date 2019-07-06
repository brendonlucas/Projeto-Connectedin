from django.db import models
from authentication.models import User

TYPE_POST = (
    ('0', 'Post'),
    ('1', 'Comment')
)

class Post(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='imagens/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reactions = models.IntegerField(default=0)
    type_post = models.CharField(max_length=1, choices=TYPE_POST, default='0')
    pub_date = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ['-pub_date']