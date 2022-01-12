from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleVeiwSet

app_name = 'news'

router = DefaultRouter()
router.register("news", ArticleVeiwSet)

urlpatterns = [
    path('api/', include(router.urls))
]