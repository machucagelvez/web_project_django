from django.shortcuts import render
from apps.blog_app.models import Post


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})
