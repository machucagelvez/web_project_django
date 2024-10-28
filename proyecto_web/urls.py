"""
URL configuration for proyecto_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from proyecto_web_app.views import home, services, store, blog, contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="Inicio"),
    path("services/", services, name="Servicios"),
    path("store/", store, name="Tienda"),
    path("blog/", blog, name="Blog"),
    path("contact/", contact, name="Contacto"),
]
