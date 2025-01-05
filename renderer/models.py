from django.db.models import CharField, Model
from django.db import models
from django.contrib.auth.models import User  # Import User model


# Create your models here.
class Poster(models.Model):

    url = CharField(max_length=256, null = True)
    name = CharField(max_length=126, null=True)
    description = CharField(max_length=256, null=True)
    director_name = CharField(max_length=126, null=True)

    def __str__(self):
        return self.url if self.url else 'No URL'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Default user (ID 1)
    poster_id = models.ForeignKey(Poster, on_delete=models.CASCADE, related_name="favorites")

    def __str__(self):
        return f"Favorite: {self.poster_id}"