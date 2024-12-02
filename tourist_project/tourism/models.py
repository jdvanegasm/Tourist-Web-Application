from django.db import models
import uuid

# users model
class User(models.Model):
    user_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    hashed_password = models.CharField(max_length = 128)
    registration_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

# countries model
class Country(models.Model):
    country_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
# cities model
class City(models.Model):
    cities_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.country.name}"
    
# posts model
class Post(models.Models):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add = True)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
# images model
class Image(models.Models):
    image_id = models.AutoField(primary_key = True)
    url = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"Image {self.image_id} for post {self.post.title}"

# tags model
class Tag(models.Model):
    tag_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
# PostTag model
class PostTag(models.Models):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)

    class Meta:
        unique_together = ['post', 'tag']

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"

#comments model
class Comment(models.Models):
    comment_id = models.AutoField(primary_key = True)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.title}"