from django.db import models

from profiles.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

class Idea(models.Model):
    user = models.ForeignKey(Profile)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1200)
    category = models.ManyToManyField(Category)
    tags = models.CharField(max_length=1200)
    create_date = models.DateTimeField(auto_now_add=True)

    likes = models.IntegerField(default=0)

class VotedOn(models.Model):
    idea = models.ForeignKey(Idea)
    user = models.ForeignKey(Profile)

class HasCategory(models.Model):
    idea = models.ForeignKey(Idea)
    category = models.ForeignKey(Category)
