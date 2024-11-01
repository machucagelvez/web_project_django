from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    # upload_to="services" indica donde se van a guardar las imagenes (crea la carpeta si no existe):
    image = models.ImageField(upload_to="services")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "service"
        verbose_name_plural = "services"

    def __str__(self):
        return self.title
