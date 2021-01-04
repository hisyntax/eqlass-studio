
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('photo-gallery/', include('photo.urls')),
    path('video-gallery/', include('video.urls')),
    path('contact/', include('contact.urls')),
    path('services/', include('service.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
