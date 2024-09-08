from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),  # List view
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Detail view
    path('books/add/', BookCreateView.as_view(), name='book_add'),  # Create view
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),  # Update view
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),  # Delete view
]
