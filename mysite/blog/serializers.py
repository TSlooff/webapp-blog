from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'comments', 'author', 'created_date', 'published_date')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_title = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = ('pk', 'post', 'post_title', 'author', 'text', 'created_date',)
