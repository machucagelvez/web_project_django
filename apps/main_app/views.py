from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "main_app/home.html")


def store(request):
    return render(request, "main_app/store.html")


def blog(request):
    return render(request, "main_app/blog.html")


def contact(request):
    return render(request, "main_app/contact.html")
