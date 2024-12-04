from rest_framework import serializers
from .models import User, Country, City, Post, Image, Tag, Comment, PostTag
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'password', 'registration_date']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Establece el hash de la contraseña
        user.save()
        return user

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_id', 'name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_id', 'name', 'country']  

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    city = CitySerializer(read_only = True)
    user = UserSerializer(read_only = True)
    
    class Meta:
        model = Post
        fields = ['post_id', 'title', 'description', 'creation_date', 'images', 'city', 'user']

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        images = validated_data.pop('images', [])
        city_data = validated_data.pop('city', None)  # Recibimos la ciudad como un diccionario
        
        # Obtener la ciudad
        city = City.objects.get(name=city_data['name'])  # Buscamos la ciudad por su nombre
        
        # Crear el post
        post = Post.objects.create(city=city, **validated_data)

        # Relacionar etiquetas al post
        for tag in tags:
            post.tags.add(tag)
        
        # Crear imágenes
        for image_url in images:
            Image.objects.create(post=post, url=image_url)
        
        return post

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'url']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user