from rest_framework import viewsets
from diary.serializers import PostSerializer
from diary.models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
