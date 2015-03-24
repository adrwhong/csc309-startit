from django.conf.urls import patterns, url, include
import profiles.urls
import accounts.urls
from . import views

from tastypie.api import Api
from .api import IdeaResource

idea_resource = IdeaResource()

urlpatterns = patterns(
    '',
    url(r'^$', views.IdeasView.as_view(), name='ideas_list'),

    url(r'^(?P<pk>\d+)/$', views.IdeaDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/vote$', views.vote, name='vote'),
    url(r'^new/$', views.new_idea, name='new'),
    url(r'^new/success/$', views.new_success, name='new_success'),
    url(r'^api/', include(idea_resource.urls)),

)
