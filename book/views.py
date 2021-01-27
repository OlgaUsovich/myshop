from django.shortcuts import render

# Create your views here.
from .models import Book, Genre, Author


def indexBook(request):
    return render(request, 'book/book.html')


def BookList(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    arr = []
    for book in books:
        arr.append({"key": book.id, "cat": book.genres.all()})
        print(book.author.all())

    print(str(arr[0]["cat"][0])+'s')

    aliases = {1: 'Пушкин', 2: 'Лоусон J.', 3: 'JK', 7: 'Happy'}

    context = {'books': books, 'ganr': arr, 'aliases': aliases, 'authors': authors}
    return render(request, 'book/book_list.html', context)
