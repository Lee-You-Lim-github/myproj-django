from django.contrib import admin
from news.models import Article

@admin.register(Article)
class AricleAdmin(admin.ModelAdmin):
    pass
