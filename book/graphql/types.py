from graphene_django import DjangoObjectType

from book.models import BookCategory, BookGenre, Book


class BookCategoryType(DjangoObjectType):
    class Meta:
        model = BookCategory
        fields = ("id", "name")


class BookGenreType(DjangoObjectType):
    class Meta:
        model = BookGenre
        fields = ("id", "name")


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "summary", "cover", "category", "genres")
