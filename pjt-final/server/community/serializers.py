from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('user_id',)