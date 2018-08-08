from django.conf.urls import include, url
from django.contrib import admin
from kimoujoonj import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    
    url(r'^$', views.home),
]



from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)