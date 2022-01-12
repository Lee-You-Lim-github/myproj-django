from rest_framework import viewsets
from news.models import Article
from news.serializers import ArticleSerializer

class ArticleVeiwSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
