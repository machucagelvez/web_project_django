from django.shortcuts import render
from apps.blog_app.models import Post, Category


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def categories(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(
        request, "blog/categories.html", {"category": category, "posts": posts}
    )
