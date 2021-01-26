from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('addarticle/', views.addarticle, name = "addarticle"),
    path('article/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.update_article, name='update_article'),
    path('delete/<int:id>', views.delete_article, name='delete_article'),
    path('', views.article_list, name='article_list'),
    path('comment/<int:id>', views.add_comment, name='add_comment'),
    path('api/', views.ArticleList.as_view()),
    path('api/<int:pk>', views.ArticleDetail.as_view()),
    path('api/create', views.ArticleCreate.as_view())
]