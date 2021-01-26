from django.contrib import admin
from .models import Article, Comment
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "comment_author", "comment_date"]
    list_display_links = ["article", "comment_date"]
    search_fields = ["article"]
    list_filter = ["article"]

    class Meta:
        model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date", "author"]

    class Meta:
        model = Article
