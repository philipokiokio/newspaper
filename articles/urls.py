from django.urls import path
from .views import (ArticleListView,ArticleDeleteView,ArticleEditView,
ArticleDetailView,ArticleCreateView)

urlpatterns= [
        path('', ArticleListView.as_view(),name = 'article_list'),
        path('<int:pk>/', ArticleDetailView.as_view(), name= 'article_detail'),
        path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
        path('<int:pk>/edit/', ArticleEditView.as_view(), name='edit'),
        path('create/', ArticleCreateView.as_view(), name='create'),
]