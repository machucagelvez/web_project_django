from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "main_app/home.html")


def store(request):
    return render(request, "main_app/store.html")
