from rest_framework import serializers
from diary.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = "__all__"