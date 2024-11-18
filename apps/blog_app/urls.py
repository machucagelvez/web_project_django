from django.urls import path

from .views import blog, categories

urlpatterns = [
    path("", blog, name="blog"),
    path("categories/<int:category_id>", categories, name="categories"),
]
