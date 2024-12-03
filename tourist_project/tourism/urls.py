from django.urls import path
from .views import (
    UserListCreateView, CountryListCreateView, CityListCreateView,
    PostListCreateView, PostDetailView, ImageListCreateView, 
    TagListCreateView, CommentListCreateView, CommentDetailView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('images/', ImageListCreateView.as_view(), name='image-list-create'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]