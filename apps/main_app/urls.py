from django.urls import path

from apps.main_app.views import home, services, store, blog, contact

urlpatterns = [
    path("", home, name="Inicio"),
    path("services/", services, name="Servicios"),
    path("store/", store, name="Tienda"),
    path("blog/", blog, name="Blog"),
    path("contact/", contact, name="Contacto"),
]
