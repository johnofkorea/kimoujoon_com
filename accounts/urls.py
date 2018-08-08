from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup),

    url(r'^super_login/$', views.super_login),
]
