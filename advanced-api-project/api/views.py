#from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book

# ListView for retrieving all books
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Customize the template if needed

# DetailView for retrieving a single book by ID
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

# CreateView for adding a new book
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']  # Define form fields
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect to book list after creating

# UpdateView for modifying an existing book
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

# DeleteView for removing a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


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
    

from rest_framework.permissions import IsAuthenticatedOrReadOnly
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