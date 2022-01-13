import json
from django.http import HttpResponse
from rest_framework import viewsets
from news.models import Article
from news.serializers import  ArticleAdminSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleAdminSerializer

   # def get_serializer_class(self):
   #     return ArticleAnomymousSerializer
   #     return ArticleGoldMembershipSerializer
   #     return ArticleAdminSerializer

# 동적인 처리를 위해(검색)
#    def get_queryset(self):
#        qs = super().get_queryset()
#        query = self.request.query_params.get("query", "")   # request.GET
#        if query:
#            qs = qs.filter(title_icontains=query)
#
#      year = self.request.query_params.get("year", "")
#      if year:
#          qs = qs.filter(created_at__year=year)
#      return qs


# Class 구현 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#  article_list = ListAPIView.as_view(
#    queryset = Article.objects.all(),
#    serializer_class = ArticleAdminSerializer
# )

# 함수 구현 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# step 1
# def article_list(request):
#    qs = Article.objects.all()

# step 2
#    serializer = ArticleSerializer(qs, many=True)
#    data = serializer.data
#     data = [
#        {
#            "id": article.id,
#            "title": article.title,
#            "content": article.content,
#            "photo": request.build_absolute_uri(article.photo.url) if article.photo else None
#        }
#        for article in qs
#     ]
#    json_string = json.dumps(data)
#    return HttpResponse(json_string)
