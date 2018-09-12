from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^count_contribution/$', views.count_contribution),
    url(r'^input/$', views.input),
]
