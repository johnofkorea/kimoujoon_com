from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^newsfactory/(?P<year_month>\S+)$', views.newsfactory),
    url(r'^thought/(?P<yy_mm_dd>\S+)$', views.thought),
    url(r'^search/$', views.search),
    url(r'^contributors/$', views.contributors),
    url(r'^contributor/(?P<user_id>\S+)$', views.contributor),
]
