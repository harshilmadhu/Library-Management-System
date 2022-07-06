from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
