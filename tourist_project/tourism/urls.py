from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserListCreateView, CountryListCreateView, CityListCreateView,
    PostListCreateView, PostDetailView, ImageListCreateView, 
    TagListCreateView, CommentListCreateView, CommentDetailView, PostByTagListView,
    PostByCountryListView, PostByCityListView, CreatePostView, RegisterUserView, SearchSuggestionsView
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
    path('api/posts/tags/<str:tag_name>/', PostByTagListView.as_view(), name = 'posts-by-tag'),
    path('api/post/countries/<str:country_name>/', PostByCountryListView.as_view(), name = 'post-by-country'),
    path('api/post/cities/<str:city_name>/', PostByCityListView.as_view(), name = 'post-by-city'),
    path('api/posts/create/', CreatePostView.as_view(), name='create_post'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('search-suggestions/', SearchSuggestionsView.as_view(), name='search-suggestions'),

]