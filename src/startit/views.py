from django.views import generic
from django.shortcuts import HttpResponse


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class BrowseIdeasPage(generic.TemplateView):
    template_name = "browse.html"


class DetailPage(generic.TemplateView):
    template_name = "detail.html"


class NewIdeaPage(generic.TemplateView):
    template_name = "new.html"

def new_success(request):
    import pdb; pdb.set_trace();
    return HttpResponse("Success!");
