from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, World!")
	
def biel(request):
	return HttpResponse("Hello, biel!")
	
def lerigou(request):
	return HttpResponse("Hello, lerigou!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })



