from django.urls import path

from apps.main_app.views import home, store, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("store/", store, name="store"),
    path("contact/", contact, name="contact"),
]

# Incluye dentro de urlpatterns la ruta para los archivos estáticos (carpeta media)
# Esto es para que se puedan acceder a los archivos de la carpeta media desde el panel de administración o desde la URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
