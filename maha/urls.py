from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('customers/', include('django.contrib.auth.urls')),
    path('customers/',include('customers.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)