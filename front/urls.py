from django.urls import path, re_path
from front.views import index, category, article, tag, archive_year, archive_month, search

urlpatterns = [
    path('', index, name='index'),
    path('category/<pk>/', category, name='category'),
    path('article/<pk>/', article, name='article'),
    path('tag/<int:pk>/', tag, name="tag"),
    path('archive/<int:year>/', archive_year, name='archive_year'),
    path('archive/<int:year>/<int:month>/', archive_month, name='archive_month'),
    re_path(r'^search/$', search, name='search')
]
