from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def books(request):
    return render(request, 'books/detail.html')

def prestamos(request):
    return render(request, 'books/detail.html')
