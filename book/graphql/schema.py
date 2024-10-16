import graphene

from book.graphql.mutations import Mutation
from book.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

__all__ =("schema",)