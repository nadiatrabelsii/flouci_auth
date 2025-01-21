from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")  
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
