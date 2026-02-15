from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone = models.CharField(max_length=15 ,blank=True)

class Post(models.Model):

    title = models.CharField(max_length=100)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    message  = models.CharField(max_length=200)

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")

    post= models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes")

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")

    created_at = models.DateTimeField(auto_now_add=True)
