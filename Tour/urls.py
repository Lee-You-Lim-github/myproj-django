from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Tour.views import SpotViewSet

app_name = 'tour'

router = DefaultRouter()
router.register("spots", SpotViewSet)

urlpatterns = [
    path('/api/', include(router.urls)),
]