import graphene
from .query import Query
from .mutations import createUserMutation

schema = graphene.Schema(query=Query, mutation=createUserMutation)