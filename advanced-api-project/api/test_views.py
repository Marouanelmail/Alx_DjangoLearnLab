from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer

class BookTests(APITestCase):
    def setUp(self):
        """Set up initial data for testing"""
        self.author = Author.objects.create(name='Author Name')
        self.book = Book.objects.create(
            title='Book Title',
            publication_year=2023,
            author=self.author
        )
        self.url = '/api/books/'

    def test_create_book(self):
        """Test creating a book"""
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book(self):
        """Test updating a book"""
        data = {
            'title': 'Updated Book Title'
        }
        response = self.client.put(f'{self.url}{self.book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        """Test retrieving a list of books"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_filter_books(self):
        """Test filtering books"""
        response = self.client.get(self.url, {'title': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        """Test searching books"""
        response = self.client.get(self.url, {'search': 'Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_ordering_books(self):
        """Test ordering books"""
        response = self.client.get(self.url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], 'Book Title')