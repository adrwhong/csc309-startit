from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

import profiles.urls
import accounts.urls

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^ideas/', include('ideas.urls', namespace='ideas')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
