from rest_framework import serializers
from Tour.models import Spot

class SpotAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = "__all__"

# 유효성 검사 - models.py