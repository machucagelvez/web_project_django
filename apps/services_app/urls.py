from django.urls import path

from .views import services
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", services, name="services"),
]
