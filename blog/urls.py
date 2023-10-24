from django.urls import path, re_path
from blog.views import *

"""
rer
5jS-D9b-ijP-4wv
"""
urlpatterns = [
    path('home/', HomePostListViewAllUsers.as_view(), name='blog_home'),
    path('', index, name='blog_index'),
    path('post/user/<str:username>', UserPostListView.as_view(), name='user_post_list'),
    path('post/new', PostCreateView.as_view(), name='post_create'),
    # path('post/<str:slug>/<int:pk>/detail', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:slug>/<int:pk>/detail', post_detail_view, name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('saved_post', all_save_view_post, name='saved_post'),
    path('post/save', saved_post_is_ajax, name='post-save'),
    path('post/like', like_post, name='post-like'),

]

