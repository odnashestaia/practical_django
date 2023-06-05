from django.urls import path, re_path
from blog.views import *

"""
rer
5jS-D9b-ijP-4wv
"""

urlpatterns = [
    path('posts/user/<str:username>', UserPostListView.as_view(), name='user_post_list'),
    path('post/new', PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/<int:pk>/detail', PostDetailView.as_view(), name='post-detail')
]