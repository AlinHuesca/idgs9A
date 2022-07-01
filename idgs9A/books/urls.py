<<<<<<< HEAD
from numbers import Integral
=======
>>>>>>> master
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='index'),
<<<<<<< HEAD
    path('books', views.seriesList, name='books'),
    path('prestamos', views.seriesList, name='prestamos'),
=======
    path('books', views.books, name='booksList'),
    path('prestamos', views.prestamos, name='prestamos'),
>>>>>>> master
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)