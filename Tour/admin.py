from django.contrib import admin
from Tour.models import Spot


@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    pass