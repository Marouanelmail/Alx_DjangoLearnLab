#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from django.shortcuts import render

# Create your views here.
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book

# Book List View - Displays a list of all books
class BookListView(ListView):
    """Handles listing all book instances"""
    model = Book
    template_name = 'book_list.html'
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to everyone, but modify access to authenticated users

# Book Detail View - Displays details for a single book instance
class BookDetailView(DetailView):
    """Handles displaying details for a specific book by ID"""
    model = Book
    template_name = 'book_detail.html'
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to everyone, but modify access to authenticated users

# Book Create View - Allows users to add a new book
class BookCreateView(CreateView):
    """Handles creation of a new book instance"""
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticated]  # Require authentication to create a book

    def form_valid(self, form):
        """
        Overrides the form_valid method to add custom validation
        For example: Ensuring that the publication year is not in the future.
        """
        if form.cleaned_data['publication_year'] > datetime.date.today().year:
            form.add_error('publication_year', 'Publication year cannot be in the future.')
            return self.form_invalid(form)
        return super().form_valid(form)

# Book Update View - Allows users to update an existing book
class BookUpdateView(UpdateView):
    """Handles updating an existing book instance"""
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticated]  # Require authentication to update a book

# Book Delete View - Allows users to delete a book
class BookDeleteView(DeleteView):
    """Handles deleting a book instance"""
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticated]  # Require authentication to delete a book

#######

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        # Add custom validation or logic here
        # Example: log data before saving
        print(f"Creating a new book: {form.cleaned_data['title']}")
        
        # Call the parent class's form_valid method to save the form data
        return super().form_valid(form)
    
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        # Custom validation or logic before updating
        return super().form_valid(form)    
    

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    permission_classes = [IsAuthenticatedOrReadOnly]

#######
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

class BookListView(generics.ListAPIView):
    """Handles listing all book instances with filtering, searching, and ordering"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering