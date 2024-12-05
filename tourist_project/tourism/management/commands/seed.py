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
        country3 = Country.objects.create(name="España")
        country4 = Country.objects.create(name="México")

        self.stdout.write("Creando ciudades...")
        city1 = City.objects.create(name="Bogotá", country=country1)
        city2 = City.objects.create(name="Buenos Aires", country=country2)
        city3 = City.objects.create(name="Madrid", country=country3)
        city4 = City.objects.create(name="Ciudad de México", country=country4)

        self.stdout.write("Creando etiquetas...")
        tag1 = Tag.objects.create(name="Aventura")
        tag2 = Tag.objects.create(name="Cultura")
        tag3 = Tag.objects.create(name="Gastronomía")
        tag4 = Tag.objects.create(name="Historia")
        tag5 = Tag.objects.create(name="Naturaleza")
        tag6 = Tag.objects.create(name="Playas")

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
        post3 = Post.objects.create(
            title="Madrid, la ciudad del arte",
            description="Disfruta de la cultura y el arte en Madrid, España.",
            city=city3,
            user=user1
        )
        post4 = Post.objects.create(
            title="La Riviera Maya",
            description="Playas y aventuras en la costa mexicana.",
            city=city4,
            user=user2
        )
        post5 = Post.objects.create(
            title="Monte de Monserrate",
            description="Una vista panorámica de Bogotá desde el monte de Monserrate.",
            city=city1,
            user=user1
        )
        post6 = Post.objects.create(
            title="La Boca, Buenos Aires",
            description="Un recorrido por el barrio más colorido de Buenos Aires.",
            city=city2,
            user=user2
        )
        post7 = Post.objects.create(
            title="El Retiro, Madrid",
            description="Un hermoso parque en el corazón de Madrid, perfecto para un paseo.",
            city=city3,
            user=user1
        )
        post8 = Post.objects.create(
            title="Chichen Itzá",
            description="Visita la famosa ciudad maya de Chichen Itzá, en México.",
            city=city4,
            user=user2
        )

        self.stdout.write("Creando etiquetas para los posts...")
        PostTag.objects.create(post=post1, tag=tag1)
        PostTag.objects.create(post=post1, tag=tag2)
        PostTag.objects.create(post=post2, tag=tag2)
        PostTag.objects.create(post=post2, tag=tag3)
        PostTag.objects.create(post=post3, tag=tag2)
        PostTag.objects.create(post=post3, tag=tag4)
        PostTag.objects.create(post=post4, tag=tag5)
        PostTag.objects.create(post=post4, tag=tag6)
        PostTag.objects.create(post=post5, tag=tag1)
        PostTag.objects.create(post=post6, tag=tag2)
        PostTag.objects.create(post=post6, tag=tag5)
        PostTag.objects.create(post=post7, tag=tag2)
        PostTag.objects.create(post=post7, tag=tag1)
        PostTag.objects.create(post=post8, tag=tag3)
        PostTag.objects.create(post=post8, tag=tag4)

        self.stdout.write("Creando imágenes para los posts...")
        post1.image_set.create(url="https://www.cepal.org/sites/default/files/styles/1920x1080/public/regionaloffice/images/bogota.jpg?itok=6GS_dObY")
        post2.image_set.create(url="https://static.cozycozy.com/images/catalog/bg/ciudad-autonoma-de-buenos-aires.jpg")
        post3.image_set.create(url="https://www.economist.com/cdn-cgi/image/width=1424,quality=80,format=auto/content-assets/images/20240824_CUP504.jpg")
        post4.image_set.create(url="https://media2.holiplus.com/3840x2880/uploads/excursion/93567/xcaret-tour-from-riviera-maya-658.jpeg")
        post5.image_set.create(url="https://monserrate.co/uploads/site/home/night-view-2x.jpg")
        post6.image_set.create(url="https://upload.wikimedia.org/wikipedia/commons/8/8b/Buenos_Aires_-_La_Boca_-_Caminito_-_200807i.jpg")
        post7.image_set.create(url="https://res.cloudinary.com/hello-tickets/image/upload/c_limit,f_auto,q_auto,w_1300/v1652924770/agdwabbva2rv0cqhsgwr.jpg")
        post8.image_set.create(url="https://www.es.kayak.com/news/wp-content/uploads/sites/47/2021/09/hisp_header-3.jpg")

        self.stdout.write("Creando comentarios...")
        Comment.objects.create(content="¡Increíble post!", post=post1, user=user2)
        Comment.objects.create(content="Me encanta Bogotá, buena recomendación", post=post1, user=user1)
        Comment.objects.create(content="Excelente información sobre Buenos Aires", post=post2, user=user1)
        Comment.objects.create(content="Un post muy útil sobre Madrid", post=post3, user=user2)
        Comment.objects.create(content="Es un destino paradisíaco, muy buena recomendación", post=post4, user=user1)
        Comment.objects.create(content="Visitar Monserrate es una experiencia única", post=post5, user=user2)
        Comment.objects.create(content="La Boca es un lugar lleno de historia y cultura", post=post6, user=user1)
        Comment.objects.create(content="Un parque espectacular para hacer ejercicio", post=post7, user=user2)
        Comment.objects.create(content="Chichen Itzá es una maravilla del mundo", post=post8, user=user1)

        self.stdout.write(self.style.SUCCESS("Datos de ejemplo creados con éxito"))