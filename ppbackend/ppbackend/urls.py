from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("jet", include("jet.urls", "jet")),
    path("api/v1/employees/", include("employees.urls", namespace="employees")),
    path("admin/", admin.site.urls),
]
