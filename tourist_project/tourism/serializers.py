from rest_framework import serializers
from .models import User, Country, City, Post, Image, Tag, Comment, PostTag
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'password', 'registration_date']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.hashed_password = make_password(password)
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
        city_data = validated_data.pop('city', None)
        
        city = City.objects.get(name=city_data['name'])
        
        post = Post.objects.create(city=city, **validated_data)

        for tag in tags:
            post.tags.add(tag)
        
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
        email = data.get("email")
        password = data.get("password")

        try:
            # Busca el usuario por correo electrónico
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Credenciales inválidas.")

        # Verifica la contraseña
        if not check_password(password, user.hashed_password):
            raise serializers.ValidationError("Credenciales inválidas.")
        return user