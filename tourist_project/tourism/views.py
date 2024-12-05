from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
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

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                "access": access_token,
                "refresh": refresh_token,
            }, status=status.HTTP_200_OK)

        return Response({
            "error": "Credenciales inválidas"
        }, status=status.HTTP_400_BAD_REQUEST)

    
class RegisterView(APIView):
    def post(self, request):
        print("Datos recibidos en la solicitud:", request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario registrado exitosamente."}, status=status.HTTP_201_CREATED)
        print("Errores del serializer:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'

class PostByTagListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            raise NotFound(detail="Etiqueta no encontrada", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(posttag__tag=tag).distinct().prefetch_related('posttag__tag')
    
class PostByCountryListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        country_name = self.kwargs['country_name']
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            raise NotFound(detail="Pais no encontrado", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(city__country=country).distinct().prefetch_related('city__country')

class PostByCityListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            raise NotFound(detail="Ciudad no encontrada", code=status.HTTP_404_NOT_FOUND)
        
        return Post.objects.filter(city=city)
    
class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        title = request.data.get('title')
        description = request.data.get('description')
        city_name = request.data.get('city')
        image_urls = request.data.get('images', [])
        tags = request.data.get('tags', [])

        try:
            city = City.objects.get(name=city_name)
        except City.DoesNotExist:
            return Response({'error': 'Ciudad no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        if Post.objects.filter(title=title, city=city).exists():
            return Response({'error': 'Un post con el mismo titulo ya existe para esta ciudad'}, 
                            status=status.HTTP_400_BAD_REQUEST)

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
                        return Response({'error': 'URL de la imagen invalida'}, status=status.HTTP_400_BAD_REQUEST)

                    Image.objects.create(url=image_url, post=post)

            if tags:
                for tag_name in tags:
                    if not isinstance(tag_name, str) or len(tag_name) > 50:
                        return Response({'error': 'Nombre de etiqueta invalido'}, status=status.HTTP_400_BAD_REQUEST)
                    try:
                        tag = Tag.objects.get(name=tag_name)
                        PostTag.objects.create(post=post, tag=tag)
                    except Tag.DoesNotExist:
                        return Response({'error': f'La etiqueta "{tag_name}" no existe'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
class CreateCommentView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden comentar

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        content = request.data.get('content')

        # Validación de existencia del post
        try:
            post = Post.objects.get(post_id=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el comentario
        comment_data = {
            'content': content,
            'post': post,
            'user': request.user
        }

        serializer = CommentSerializer(data=comment_data)
        if serializer.is_valid():
            comment = serializer.save()

            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchSuggestionsView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', '')
        if query:
            countries = Country.objects.filter(name__icontains=query)
            cities = City.objects.filter(name__icontains=query)
            tags = Tag.objects.filter(name__icontains=query)

            country_names = [country.name for country in countries]
            city_names = [city.name for city in cities]
            tag_names = [tag.name for tag in tags]

            return Response({
                'countries': country_names,
                'cities': city_names,
                'tags': tag_names
            })

        return Response({'error': 'No se proporcionó ningún parámetro de consulta'}, status=status.HTTP_400_BAD_REQUEST)