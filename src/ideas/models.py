from django.db import models
from profiles.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=50)


class Idea(models.Model):
    user = models.ForeignKey(Profile)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1200)
    categories = models.ManyToManyField(Category)
    tags = models.CharField(max_length=1200)
    create_date = models.DateTimeField('Creation Date')

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)



