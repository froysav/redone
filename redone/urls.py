from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from redone import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
# urlpatterns += i18n_patterns(
#     path('', include("app.urls"),name='app')
# )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                        document_root=settings.MEDIA_ROOT)
