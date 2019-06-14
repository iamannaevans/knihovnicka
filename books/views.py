from django.shortcuts import render

from .models import Book
from .models import Author

# Create your views here.
def book_detail_view(request):
    book = Book.objects.get(id=1)
    print(book.title)
    context = {
        'object': book
    }
    return render(request, 'book/detail.html', context)

def author_detail_view(request):
    author = Author.objects.get(id=1)
    context = {
        'object': author
    }
    return render(request, 'author/detail.html', context)
