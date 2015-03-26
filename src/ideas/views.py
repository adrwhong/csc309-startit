from random import randint

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404, HttpResponse, redirect, render
from django.utils import timezone

from sortable_listview import SortableListView

from chartjs.views.lines import BaseLineChartView

from .forms import NewIdeaForm, EditIdeaForm
from ideas.models import Idea, Category, VotedOn, HasCategory
from profiles.models import Profile

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels."""
        res = [row['name'] for row in Category.objects.values()]
        res.sort()
        return res

    def get_data(self):
        """Return 3 dataset to plot."""
        categories = {r['id']: r['name'] for r in Category.objects.values()}

        counts = {}
        for r in HasCategory.objects.values():
            name = categories[r['category_id']]
            if name in counts:
                counts[name] += 1
            else:
               counts[name] = 1


        res = []
        for label in self.get_labels():
            if label in counts:
                res.append(counts[label])
            else:
                res.append(0)

        return [res]


class StatsPageView(TemplateView):
    template_name = "stats.html"


class IdeasView(SortableListView):
    model = Idea
    template_name = "ideas.html"
    allowed_sort_fields = {'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
                           'create_date': {'default_direction': '-',
                                           'verbose_name': 'Published On'}}
    default_sort_field = 'create_date'

    def get_queryset(self):
        qs = super(SortableListView, self).get_queryset()
        qs = qs.order_by(self.sort)

        if len(self.args) == 2:
            q = self.args[1]
            if self.args[0] == 'tags':
                return qs.filter(tags__icontains=q)

            elif self.args[0] == 'category':
                return qs.filter(hascategory__category__name__icontains=q)
        else:
            return qs.all()

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


