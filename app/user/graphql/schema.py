import graphene
from  .query import Query
from .mutations import Mutation

class Query(Query, graphene.ObjectType):
    pass

class Mutation(Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
print(schema)

print("djmdfvbjh")
# schema.execute('''
               
#                mutation myFirstMutation {
#    createUser(
#         refId:"def@gmail.com",
#         password:"qwerty@Root"
#     ) {
#        res
#     }
# }
               
#                ''')

