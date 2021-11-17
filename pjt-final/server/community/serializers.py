from rest_framework import serializers
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('user_id',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'post_id', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('post_id', 'user_id')