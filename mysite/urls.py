from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("series/", include("series.urls")),
    path("admin/", admin.site.urls),
]
