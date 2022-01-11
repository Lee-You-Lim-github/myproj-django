from django.contrib import admin

from diary.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass