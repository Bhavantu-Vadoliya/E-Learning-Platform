from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "website/index.html")
    # return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("Hello, from About !")
def contact(request):
    return HttpResponse("Hello, from Contact !")