from django.conf.urls import patterns, url
import profiles.urls
import accounts.urls
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IdeasPage.as_view(), name='ideas_list'),
    url(r'^detail/$', views.DetailPage.as_view(), name='detail'),
    url(r'^new/$', views.NewIdeaPage.as_view(), name='new'),
    url(r'^new/success/$', views.new_success, name='new_success'),
)

