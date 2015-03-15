from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^browse/$', views.BrowseIdeasPage.as_view(), name='browse'),
    url(r'^detail/$', views.DetailPage.as_view(), name='detail'),
    url(r'^new/$', views.NewIdeaPage.as_view(), name='new'),
    url(r'^new/success$', views.new_success, name='new_success'),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
