from django.db.models import Q
from django.shortcuts import get_object_or_404

from book.models import Book, BookCategory, BookGenre


def resolve_all_books(search):
    queryset = Book.objects.select_related("category").prefetch_related("genres").all()
    if search:
        # queryset = queryset.annotate(search= SearchVector('title','summary','category__name','genres__name')).filter(search=search)

        queryset = queryset.filter(Q(title__contains=search)
                                   | Q(summary__contains=search)
                                   | Q(category__name__contains=search)
                                   | Q(genres__name__contains=search)
                                   ).distinct()
    return queryset


def resolve_categories(id):
    queryset = BookCategory.objects.all()
    if id:
        queryset = queryset.filter(pk=id)
    return queryset


def resolve_genres():
    queryset = BookGenre.objects.all()
    return queryset


def resolve_genre(id):
    object = get_object_or_404(BookGenre, pk=id)
    return object
