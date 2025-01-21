from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_api_key.models import AbstractAPIKey


class User(AbstractUser):
    pass 

class UserAPIKey(AbstractAPIKey):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_api_key")


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
