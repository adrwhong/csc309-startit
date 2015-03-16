from django.views import generic
from django.shortcuts import HttpResponse


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
