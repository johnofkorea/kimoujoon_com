from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^journal/$', views.journal),
    url(r'^wnotebook/$', views.wnotebook),
    url(r'^wnote/(?P<chapter_id>\S+)$', views.wnote),
    url(r'^wnoteq/(?P<order>\S+)$', views.wnoteq),

    url(r'^wrecord/$', views.wrecord),
]
