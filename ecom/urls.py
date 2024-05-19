from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

admin.site.site_header = "Share Book Admin Dashboard"
admin.site.site_title = "Share Book Admin Portal"
admin.site.site_header = "Welcome to Share Book Admin Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
