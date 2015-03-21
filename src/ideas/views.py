from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render, HttpResponse
from django.utils import timezone

from profiles.models import Profile
from ideas.models import Idea, Category

from .forms import NewIdeaForm

class IdeasView(generic.ListView):
    model = Idea
    template_name = "ideas.html"


class IdeaDetailView(generic.DetailView):
    model=Idea
    template_name = "detail.html"


def new_idea(request):
    return render(request, 'new.html',
        {'form': NewIdeaForm()})

@login_required
def new_success(request):
    if request.POST:
        profile = Profile(user=request.user)
        title = request.POST["title"]
        desc = request.POST["description"]
        categories = request.POST["categories"]
        tags = request.POST["tags"]


        i = Idea(user=profile,
                 title=title,
                 description=desc,
                 tags=tags,
                 create_date=timezone.now())

        i = i.save()

    #REDIRECT SOMEWHERE.
    return HttpResponse("Success!")

@login_required
def like_dislike(request):
    import pdb; pdb.set_trace()
    return HttpResponse("Success!")
