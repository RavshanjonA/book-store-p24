import graphene
import graphql_jwt
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required, permission_required

from book.graphql.mutates import create_book_mutate, update_book_mutate, delete_book_mutate, create_user_mutate, \
    create_genre_mutate, update_genre_mutate
from book.graphql.object_permission import is_owner_permission
from book.graphql.types import BookType, UserType, BookGenreType


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


class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    genre = graphene.Field(BookGenreType)

    @classmethod
    @permission_required("book.add_bookgenre")
    def mutate(cls, root, info, name):
        genre = create_genre_mutate(name)
        return cls(genre=genre)

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    genre = graphene.Field(BookGenreType)

    @classmethod
    @login_required
    @is_owner_permission
    def mutate(cls, root, info, id, name):
        genre = update_genre_mutate(id, name)
        return cls(genre=genre)


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
        return cls(success=status)


class RegisterUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        password2 = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = create_user_mutate(**kwargs)
        return RegisterUser(user=user)


class Mutation(graphene.ObjectType):
    # book

    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    # genre
    create_genre = CreateGenre.Field()
    update_genre = UpdateGenre.Field()

    # user
    register_user = RegisterUser.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# registerUser(username, password, password2, email){
#     user{
#       username
#       email
#       is_staff
#       is_active
#     }
# }
