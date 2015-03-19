from django.db import models
from profiles.models import Profile

class Idea(models.Model):
    user = models.ForeignKey(Profile)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1200)
    tags = models.CharField(max_length=1200)
    create_date = models.DateTimeField('Creation Date')

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    #how do we implement how many people voted on this?
    #voted = models.OneToManyField(Profile)

#class VotedOn(models.Model):
#    pass

