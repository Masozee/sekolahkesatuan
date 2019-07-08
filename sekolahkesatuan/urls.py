from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

admin.sites.AdminSite.site_header = 'Sekolah Kesatuan'
admin.sites.AdminSite.site_title = 'Sekolah Kesatuan'
admin.sites.AdminSite.index_title = 'Sekolah Kesatuan'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumni.url')),
]


urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)