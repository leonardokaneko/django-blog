from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>', views.post, name='post'),
    path('busca/', views.SearchResultsView.as_view(), name='search_results'),
    path('autor/', views.author_find, name='author_find')
]
