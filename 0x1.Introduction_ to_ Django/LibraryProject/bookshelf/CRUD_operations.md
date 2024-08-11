>>> from bookshelf.models import Book
>>> book = Book( title = "1984", author = "George Orwell",  publication_year = "1949")
>>> book.save()
>>> exit()

>>> from bookshelf.models import Book
>>>book = Book.objects.get(title="1984")


>>>book = Book.objects.get(title="1984")
>>>book.title = "Nineteen Eighty-Four"
>>>book.save()

>>>book = Book.objects.get(title="1984")
>>>book.delete()


