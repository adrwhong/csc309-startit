from django.core import serializers
from django.views import generic
from django.shortcuts import HttpResponse

import json

from ideas.models import Category

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class APIDemoPage(generic.TemplateView):
    template_name = "api-demo.html"


def get_categories_json(request):
    categories = Category.objects.all()
    data = serializers.serialize('json', categories)
    print(data)
    return HttpResponse(json.dumps(json.loads(data)), content_type='application/json')
