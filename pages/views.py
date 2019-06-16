from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
		# return HttpResponse('<h1>Hello World</h1>')
        return render(request, 'home.html', {})

def authors_view(request, *args, **kwargs):
		return render(request, 'authors.html', {})
