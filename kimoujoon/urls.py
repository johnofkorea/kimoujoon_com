from django.conf.urls import include, url
from django.contrib import admin
from korean import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^kr/', include('korean.urls')),
    url(r'^en/', include('english.urls')),
    url(r'^fr/', include('french.urls')),
    url(r'^jp/', include('japanese.urls')),
    url(r'^adm/', include('adm.urls')),
    url(r'^$', views.home),
]



from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)