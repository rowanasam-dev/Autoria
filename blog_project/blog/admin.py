from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model_year', 'category', 'author', 'created_at')
    list_filter = ('category', 'brand')
    search_fields = ('title', 'brand', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')