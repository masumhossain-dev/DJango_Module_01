from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.gTemp),
    path("students/", include("students.urls")),
    path("teachers/", include("teachers.urls")),
]
