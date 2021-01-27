from django.contrib import admin
from .models import Book, Author, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Genre, GenreAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'slug', 'country']
    prepopulated_fields = {'slug': ('surname',)}


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'year', 'pages', 'published_by', 'image', 'description']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)

