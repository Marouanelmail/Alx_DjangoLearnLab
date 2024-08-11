from django.contrib import admin 
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the list display to show title, author, and published date
    list_display = ('title', 'author', 'publication_year')

    # Add list filters for author and published date
    list_filter = ('author', 'publication_year')

    # Enable search by title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin configuration
admin.site.register(Book, BookAdmin)
