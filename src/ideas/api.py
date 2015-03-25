from tastypie.resources import ModelResource
from .models import Idea

import datetime
import time

class IdeaResource(ModelResource):
    class Meta:
        queryset = Idea.objects.all().order_by('-likes')
        resource_name = 'idea'
        #max_limit = k

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(IdeaResource, self).build_filters(filters)

        if 'start' in filters:
            query = filters['start']
            start = datetime.datetime(*time.strptime(query, "%m-%d-%y")[:6])
            orm_filters['create_date__gte'] = start


        if 'end' in filters:
            query = filters['end']
            end = datetime.datetime(*time.strptime(query, "%m-%d-%y")[:6])
            orm_filters['create_date__lte'] = end

        return orm_filters
