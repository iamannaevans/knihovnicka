from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    # books = models.ForeignKey(Book, on_delete=models.CASCADE)
    # -- tohle udela dropdown, ale ja chi aby to vyistovalo automaticky vsechny knihy s timto autorem

class Book(models.Model):
    title = models.CharField(max_length=60)
    year = models.DateField()
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.CharField(max_length=60, blank=True, null=False)
