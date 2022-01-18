import json
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from news.models import Article
from news.serializers import  ArticleAdminSerializer


# list, detail, create, update, delete를 1개 ViewSet에서 지원
# 비인증 : list, detail  --(GET) // 인증 : create, update, delete
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class= ArticleAdminSerializer
    # permission_classes = [AllowAny]   # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):

        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

# 원래 form에서 유효성 검사 시, ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#     def article_new(request):
#         if request.method == "POST":
#             form = ArticleForm(request.POST, request.FILES)
#             if form.is_valid():
#                 article = form.save(commit=False)  --> user필드를 받지 않고 저장할 때
#                 article.author = request.user
#                 article.save()
#                 return redirect(...)
#         else:
#             form = ArticleForm()

# 저장 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지원을 지원합니다.
        serializer.save(author=self.request.user)
















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
