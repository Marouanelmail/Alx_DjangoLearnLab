import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == "__main__":
    # Change these to test with your actual data
    print("Books by Author:")
    for book in get_books_by_author('Author Name'):
        print(book.title)

    print("\nBooks in Library:")
    for book in get_books_in_library('Library Name'):
        print(book.title)

    print("\nLibrarian for Library:")
    librarian = get_librarian_for_library('Library Name')
    print(librarian.name)