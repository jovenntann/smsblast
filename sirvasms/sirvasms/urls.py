from django.conf.urls import url,include
from django.contrib import admin

from sirvasmsapp import views
from django.conf.urls import handler404, handler500

# MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^',include('sirvasmsapp.urls')),
    url(r'^portal/',include('sirvasmsapp.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
handler500 = views.error_500