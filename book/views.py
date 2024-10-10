from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from book.models import BookCategory, Book
from book.serializers import BookCategorySerializer, BookSerializer


class BookCategoryViewSet(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
