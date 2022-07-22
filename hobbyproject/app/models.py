from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    # from_time = models.DateTimeField(null=True)
    # to_time = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.content
    
# class Comment(models.Model):
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     time = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
