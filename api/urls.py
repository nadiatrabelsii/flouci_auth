from django.urls import path
from .views import  PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
