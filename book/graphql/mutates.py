from readline import get_endidx
from tokenize import generate_tokens
from unicodedata import category

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from book.models import BookCategory, BookGenre, Book


def create_book_mutate(title, summary, category, genres, cover):
    category = BookCategory.objects.get(id=category)
    genres = BookGenre.objects.filter(id__in=genres)
    book = Book(
        title=title,
        summary=summary,
        cover=cover,
        category=category
    )
    book.save()
    book.genres.set(genres)
    return book


# is, ==
def update_book_mutate(id, **kwargs):
    book = get_object_or_404(Book, pk=id)
    genres = kwargs.pop("genres", None)
    category = kwargs.pop("category", None)
    for key, value in kwargs.items():
        setattr(book, key, value)
    if genres is not None:
        book.genres.set(genres)
    if category is not None:
        object = get_object_or_404(BookCategory, id=category)
        book.category = object
    book.save()
    return book


def delete_book_mutate(id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    return True


def create_genre_mutate(name):
    genre = BookGenre.objects.create(name=name)
    return genre

def update_genre_mutate(id, name):
    genre = get_object_or_404(BookGenre, id=id)
    genre.name=name
    genre.save()
    return genre


def create_user_mutate(username, password, password2, email):
    if password != password2:
        raise Exception("passwords must be match")
    if User.objects.filter(username=username).exists():
        raise Exception(f"{username} username already registered")
    user = User.objects.create_user(username=username, email=email)
    user.set_password(password)
    user.save()
    return user
