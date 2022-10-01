from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .settings import env

urlpatterns = [
    path("admin/", admin.site.urls),
    path("budget/", include("budget.urls")),
    path("user/", include("user.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if env("DEBUG"):
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
