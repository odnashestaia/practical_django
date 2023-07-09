from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('author/create', author_create, name='author_create'),
    path('author/list', AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
]