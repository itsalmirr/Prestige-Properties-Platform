from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RegisterUserAPIView, LoginUserAPIView

app_name = "identity"

urlpatterns = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", LoginUserAPIView.as_view(), name="login"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
