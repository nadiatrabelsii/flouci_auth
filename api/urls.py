from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, CustomLoginView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/token/', CustomLoginView.as_view(), name='token-obtain'), 
]
