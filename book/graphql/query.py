import graphene

from book.graphql.resolvers import resolve_all_books, resolve_categories, resolve_genres, resolve_genre
from book.graphql.types import BookType, BookCategoryType, BookGenreType


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_books = graphene.List(BookType, search=graphene.String())
    categories = graphene.List(BookCategoryType, id=graphene.Int())
    genres = graphene.List(BookGenreType)
    genre = graphene.Field(BookGenreType, id=graphene.Int(required=True))

    def resolve_all_books(root, info, search=None, **kwargs):
        return resolve_all_books(search)

    def resolve_categories(root, info, id=None, **kwargs):
        return resolve_categories(id)

    def resolve_genres(root, info, **kwargs):
        return resolve_genres()

    def resolve_genre(root, info, id, **kwargs):
        return resolve_genre(id=id)
