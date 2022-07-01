from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def books(request):
<<<<<<< HEAD
    return render(request, 'books/detail.html')

def prestamos(request):
    return render(request, 'books/detail.html')
=======
    return render(request, 'books/books.html')

def prestamos(request):
    return render(request, 'books/prestamos.html')
>>>>>>> master
