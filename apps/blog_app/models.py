from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blog", null=True, blank=True)
    # Relación uno a muchos entre el usuario y Post:
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("id",)
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title
