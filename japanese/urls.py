from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^newsfactory/(?P<year_month>\S+)$', views.newsfactory),
    url(r'^search/$', views.search),
]
