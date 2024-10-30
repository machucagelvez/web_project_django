from django.urls import path

from apps.main_app.views import home, services, store, blog, contact

urlpatterns = [
    path("", home, name="home"),
    path("services/", services, name="services"),
    path("store/", store, name="store"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
]
