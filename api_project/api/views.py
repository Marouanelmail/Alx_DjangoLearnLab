#from django.shortcuts import render

# Create your views here.
from rest_framework.generics import genericsListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(genericsListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer