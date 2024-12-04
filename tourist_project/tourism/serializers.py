from rest_framework import serializers
from .models import User, Country, City, Post, Image, Tag, Comment, PostTag
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ['title', 'description', 'city_id', 'user_id', 'tags', 'images']

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        images = validated_data.pop('images', [])
        
        # Crear el post
        post = Post.objects.create(**validated_data)

        # Relacionar etiquetas existentes al post
        for tag in tags:
            post.tags.add(tag)
        
        # Crear imágenes
        for image_url in images:
            Image.objects.create(post=post, url=image_url)
        
        return post

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

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