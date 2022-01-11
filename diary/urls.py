from django.urls import path, include
from rest_framework.routers import DefaultRouter
from diary.views import PostViewSet

app_name = 'diary'

router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]