from django.urls import path

from .views import indexBook, BookList

app_name = 'book'
urlpatterns = [
    path('', indexBook, name='book'),
    path('books/', BookList, name='book_list'),
]
