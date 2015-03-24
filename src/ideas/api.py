from tastypie.resources import ModelResource
from .models import Idea


class IdeaResource(ModelResource):
    class Meta:
        queryset = Idea.objects.all()
        resource_name = 'idea'
