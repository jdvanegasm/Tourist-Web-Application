from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from tourism.models import User, Country, City, Tag, Post, Comment, PostTag
import uuid

class Command(BaseCommand):
    help = 'Puebla la base de datos con datos de ejemplo'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creando usuarios...")
        user1 = User.objects.create(
            user_id=uuid.uuid4(),
            name="Juan Pérez",
            email="juan@example.com",
            hashed_password=make_password("contraseña123")  # Usamos hashed_password en lugar de password
        )
        user2 = User.objects.create(
            user_id=uuid.uuid4(),
            name="Ana Gómez",
            email="ana@example.com",
            hashed_password=make_password("contraseña456")
        )

        self.stdout.write("Creando países...")
        country1 = Country.objects.create(name="Colombia")
        country2 = Country.objects.create(name="Argentina")

        self.stdout.write("Creando ciudades...")
        city1 = City.objects.create(name="Bogotá", country=country1)
        city2 = City.objects.create(name="Buenos Aires", country=country2)

        self.stdout.write("Creando etiquetas...")
        tag1 = Tag.objects.create(name="Aventura")
        tag2 = Tag.objects.create(name="Cultura")
        tag3 = Tag.objects.create(name="Gastronomía")

        self.stdout.write("Creando posts...")
        post1 = Post.objects.create(
            title="Explorando Bogotá",
            description="Una experiencia única en la capital de Colombia.",
            city=city1,
            user=user1
        )
        post2 = Post.objects.create(
            title="Recorriendo Buenos Aires",
            description="Una ciudad llena de historia y cultura.",
            city=city2,
            user=user2
        )

        self.stdout.write("Creando etiquetas para los posts...")
        PostTag.objects.create(post=post1, tag=tag1)
        PostTag.objects.create(post=post1, tag=tag2)
        PostTag.objects.create(post=post2, tag=tag2)
        PostTag.objects.create(post=post2, tag=tag3)

        self.stdout.write("Creando imágenes para los posts...")
        post1.image_set.create(url="https://2182029.fs1.hubspotusercontent-na1.net/hubfs/2182029/Centro%20de%20la%20ciudad%20-%20El%20centro%20de%20Bogot%C3%A1-Bogot%C3%A1%20de%20noche.jpg")
        post2.image_set.create(url="https://arc-anglerfish-arc2-prod-infobae.s3.amazonaws.com/public/EWRWZLV7FZEM7C24TIEPFBJCP4.jpg")

        self.stdout.write("Creando comentarios...")
        Comment.objects.create(content="¡Increíble post!", post=post1, user=user2)
        Comment.objects.create(content="Me encanta Bogotá, buena recomendación", post=post1, user=user1)
        Comment.objects.create(content="Excelente información sobre Buenos Aires", post=post2, user=user1)

        self.stdout.write(self.style.SUCCESS("Datos de ejemplo creados con éxito"))