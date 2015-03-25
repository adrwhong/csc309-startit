from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404, HttpResponse, redirect

from django.core.urlresolvers import reverse
from django.utils import timezone

from profiles.models import Profile
from ideas.models import Idea, Category, VotedOn, HasCategory

from .forms import NewIdeaForm, EditIdeaForm

from sortable_listview import SortableListView


class IdeasView(SortableListView):
    model = Idea
    template_name = "ideas.html"
    allowed_sort_fields = {'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
                           'create_date': {'default_direction': '-',
                                           'verbose_name': 'Published On'}}
    default_sort_field = 'create_date'

    def get_context_data(self, **kwargs):
        context = super(IdeasView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class IdeaDetailView(DetailView):
    model=Idea
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()

        context['is_owner'] = super(IdeaDetailView, self).get_object().user == Profile(user=self.request.user)

        return context

@login_required
def new_idea(request):
    return render(request, 'new.html',
        {'form': NewIdeaForm()})

class IdeaUpdateView(UpdateView):
    model = Idea
    template_name = "edit.html"
    form_class = EditIdeaForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('ideas:detail', kwargs={'pk': pk})

@login_required
def new_success(request):
    if request.POST:
        profile = Profile(user=request.user)
        title = request.POST["title"]
        desc = request.POST["description"]
        categories = request.POST.getlist("categories")
        tags = request.POST["tags"]

        idea = Idea.objects.create(user=profile,
                 title=title,
                 description=desc,
                 tags=tags)
        idea.save()

        for category in categories:
            category = get_object_or_404(Category, name=category)
            has_c = HasCategory.objects.create(idea=idea, category=category)
            has_c.save()

    #redirect to the detail page.
    return redirect('ideas:detail', pk=idea.pk)
    #return render(HttpResponse("Success! %s" % categories)

@login_required
def vote(request, pk):
    profile = Profile(user=request.user)
    idea = Idea(pk=pk)
    voted = VotedOn.objects.filter(idea=idea, user=profile).count() > 0

    if not voted:
        voted = VotedOn(idea=idea, user=profile)
        voted.save()
        return HttpResponse(True)
    else:
        return HttpResponse(False)

