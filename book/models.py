from django.db import models

# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:genre_list', args=[self.slug])


class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    surname = models.CharField(max_length=200, db_index=True)
    genre = models.ManyToManyField(Genre)
    country = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.surname + ' ' + self.name

    def get_absolute_url(self):
        return reverse('book:author_list', args=[self.slug])


class Book(models.Model):
    CHOICES = (
        (2019, '2019'), (2020, '2020'), (2021, '2021')
    )
    genres = models.ManyToManyField(Genre, related_name='genre')
    author = models.ManyToManyField(Author, related_name='author')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='book/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    year = models.PositiveIntegerField(choices=CHOICES)
    description = models.TextField(blank=True)
    published_by = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:book_list', args=[self.slug])

