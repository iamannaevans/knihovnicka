from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)

    # Get author url by id
    def get_author_url(self):
        return reverse('author_detail_view', kwargs={'id': self.id})


class Book(models.Model):
    title = models.CharField(max_length=60)
    year = models.DateField()
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.CharField(max_length=60, blank=True, null=False)

    # Get book url by id
    def get_book_url(self):
        return reverse('book_detail_view', kwargs={'id': self.id})
