from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('user/<str:username>', UserDiscussionListView.as_view(), name='user_discussion_list'),
    # # path('new', DiscussionCreateView.as_view(), name='discussion-view'),
    # path('<str:slug>/<int:pk>/detail', DiscussionDetailView.as_view(), name='discussion-detail'),
    # path('create', discussion_create, name='create')
]