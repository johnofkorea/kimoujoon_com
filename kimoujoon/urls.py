from django.conf.urls import include, url
from django.contrib import admin
from kimoujoonj import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    
    url(r'^newsfactory/(?P<year_month>\S+)$', views.newsfactory),
    url(r'^$', views.home),
    
    url(r'^kr/newsfactory/(?P<year_month>\S+)$', views.newsfactory_kr),
    url(r'^kr/$', views.home_kr),
]



from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)