from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Book
from .models import Author

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

# View of book list
def book_list_view(request):
    queryset = Book.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'book/book_list.html', context)

# View of author list
def author_list_view(request):
    queryset = Author.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'author/author_list.html', context)

# Get books by id
def book_dynamic_lookup_view(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        'book': book
    }
    return render(request, 'book/detail.html', context)

# Get authors by id
def author_dynamic_lookup_view(request, id):
    author = get_object_or_404(Author, id=id)
    books = Book.objects.filter(writer__id=id)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author/detail.html', context)

# Search view
def search(request):
    template = 'book/book_list.html'
    query = request.GET.get('q')
    results = Book.objects.filter(Q(title__icontains=query))
    context = {
        'object_list': results,
    }
    return render(request, template, context)
