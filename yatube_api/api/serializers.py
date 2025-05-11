from rest_framework import serializers
from posts.models import Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
