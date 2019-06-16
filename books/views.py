from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Book
from .models import Author

# Create your views here.
def book_list_view(request):
    queryset = Book.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'book/book_list.html', context)

def author_list_view(request):
    queryset = Author.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'author/author_list.html', context)

def book_dynamic_lookup_view(request, id):
    obj = get_object_or_404(Book, id=id)
    context = {
        'object': obj
    }
    return render(request, 'book/detail.html', context)

def author_dynamic_lookup_view(request, id):
    obj = get_object_or_404(Author, id=id)
    books = Book.objects.filter(writer__id=id)
    context = {
        'object': obj,
        'books': books
    }
    return render(request, 'author/detail.html', context)

def search(request):
    template = 'book/book_list.html'
    query = request.GET.get('q')
    results = Book.objects.filter(Q(title__icontains=query))
    context = {
        'object_list': results,
    }
    return render(request, template, context)
