from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

import profiles.urls
import accounts.urls
from . import views

from tastypie.api import Api
from .api import IdeaResource

idea_resource = IdeaResource()

urlpatterns = patterns(
    '',
    url(r'^$', views.IdeasView.as_view(), name='ideas_list'),

    url(r'^(?P<pk>\d+)/view/$', login_required(views.IdeaDetailView.as_view()), name='detail'),
    url(r'^(?P<pk>\d+)/vote/$', login_required(views.vote), name='vote'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(views.IdeaUpdateView.as_view()), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(views.IdeaDeleteView.as_view()), name='delete'),
    url(r'^new/$', views.new_idea, name='new'),
    url(r'^new/success/$', login_required(views.new_success), name='new_success'),

    #stats
    url(r'^stats/$', views.StatsPageView.as_view(), name='stats'),
    url(r'^stats/json$', views.LineChartJSONView.as_view(), name='stats_json'),

    #idea filters
    url(r'^(tags|category)/([\w-]+)/$', views.IdeasView.as_view(), name='ideas_list'),



    url(r'^api/', include(idea_resource.urls)),

)
