from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/proccesor/proc/get/', include('proccesor.urls')),
    path('admin/videokarta/videocard/get/', include('videokarta.urls')),
    path('admin/motherboard/motherboard/get/', include('motherboard.urls')),
    path('admin/OP/operative/get/', include('OP.urls')),
    path('admin/', admin.site.urls),
    path('', include('tovar.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

