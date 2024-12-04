from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User, Country, City, Post, Image, Tag, Comment, PostTag
from .serializers import (
    UserSerializer, CountrySerializer, CitySerializer,
    PostSerializer, ImageSerializer, TagSerializer,
    CommentSerializer, LoginSerializer
)

# Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Countries
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# Cities
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Images
class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# Tags
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# Comments
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostByTagListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            raise NotFound(detail="Tag not found", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(posttag__tag=tag).distinct().prefetch_related('posttag__tag')

class PostByCountryListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        country_name = self.kwargs['country_name']
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            raise NotFound(detail="Country not found", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(city__country=country).distinct().prefetch_related('city__country')

class PostByCityListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            raise NotFound(detail="City not found", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(city=city)
    
class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        city_name = request.data.get('city')
        image_urls = request.data.get('images', [])
        tags = request.data.get('tags', [])

        if Post.objects.filter(title=title).exists():
            raise ValidationError({'title': 'A post with this title already exists.'})

        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)

        post_data = {
            'title': title,
            'description': description,
            'city': city,
            'user': request.user
        }

        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            post = serializer.save()

            if image_urls:
                for image_url in image_urls:
                    if not isinstance(image_url, str) or len(image_url) > 255:
                        return Response({'error': 'Invalid image URL'}, status=status.HTTP_400_BAD_REQUEST)
                    Image.objects.create(url=image_url, post=post)

            if tags:
                for tag_name in tags:
                    if not isinstance(tag_name, str) or len(tag_name) > 50:
                        return Response({'error': 'Invalid tag name'}, status=status.HTTP_400_BAD_REQUEST)
                    try:
                        tag = Tag.objects.get(name=tag_name)
                        post.tags.add(tag)
                    except Tag.DoesNotExist:
                        return Response({'error': f'Tag "{tag_name}" does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            # Generar los tokens
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Devolver los tokens
            return Response({
                'access': access_token,
                'refresh': refresh_token,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)