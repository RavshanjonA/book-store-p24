import graphene
from graphene_file_upload.scalars import Upload

from book.graphql.mutates import create_book_mutate, update_book_mutate, delete_book_mutate
from book.graphql.types import BookType
from book.models import BookCategory, BookGenre, Book


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        summary = graphene.String(required=True)
        cover = Upload(required=True)
        category = graphene.Int(required=True)
        genres = graphene.List(graphene.ID, required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, title, summary, category, genres, cover):
        book = create_book_mutate(title, summary, category, genres, cover)
        return CreateBook(book=book)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        summary = graphene.String()
        # file = Upload(required=True)
        category = graphene.Int()
        genres = graphene.List(graphene.ID, )

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        book = update_book_mutate(id, **kwargs)
        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Field(graphene.Boolean)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        status = delete_book_mutate(id)
        return DeleteBook(success=status)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()
