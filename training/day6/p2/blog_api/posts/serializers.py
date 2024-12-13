from rest_framework import serializers
from .models import Author, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'user', 'bio', 'website', 'created_at', 'posts_count']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'status'] 