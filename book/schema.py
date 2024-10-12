import graphene
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from graphene_django import DjangoObjectType

from book.models import Book, BookCategory, BookGenre


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


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_books = graphene.List(BookType, search=graphene.String())
    categories = graphene.List(BookCategoryType, id=graphene.Int())

    def resolve_all_books(root, info, search=None, **kwargs):
        queryset = Book.objects.all()
        if search:
            # queryset = queryset.annotate(search= SearchVector('title','summary','category__name','genres__name')).filter(search=search)

            queryset = queryset.filter(Q(title__contains=search)
                                       |Q(summary__contains=search)
                                       |Q(category__name__contains=search)
                                       |Q(genres__name__contains=search)
                                       ).distinct()
        return queryset

    def resolve_categories(root, info, id=None, **kwargs):
        queryset = BookCategory.objects.all()
        if id:
            queryset = queryset.filter(pk=id)
        return queryset


schema = graphene.Schema(query=Query)
