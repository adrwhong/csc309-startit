from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render, HttpResponse
from django.utils import timezone

from profiles.models import Profile
from ideas.models import Idea

class IdeasPage(generic.TemplateView):
    template_name = "ideas.html"


class DetailPage(generic.TemplateView):
    template_name = "detail.html"


class NewIdeaPage(generic.TemplateView):
    template_name = "new.html"

@login_required
def new_success(request):
    import pdb; pdb.set_trace();

    if request.POST:
        profile = Profile(user=request.user)
        title = request.POST["title"]
        desc = request.POST["description"]
        tags = request.POST["tags"]

        i = Idea(user=profile,
                 title=title,
                 description=desc,
                 tags=tags,
                 create_date=timezone.now())
        i = i.save()

    import pdb; pdb.set_trace();

    return HttpResponse("Success!")
