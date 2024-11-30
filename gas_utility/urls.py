from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Include URLs from the service_requests app
    path('', include('service_requests.urls')),
    path('logout/', LogoutView.as_view(), name='logout'), # type: ignore
]

# Serving media files during development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)