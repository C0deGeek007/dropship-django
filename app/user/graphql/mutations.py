import graphene
from django.contrib.auth import get_user_model
from .type import UserType


class createUser(graphene.Mutation):
    
    user =  graphene.Field(lambda:UserType)
    ok = graphene.Boolean()
    
    class Arguments:
        refId = graphene.String()
        password = graphene.String()
    
    def mutate(root, info, refId, password):
        user = get_user_model().objects.create_user(refId=refId,password=password)
        # user = UserType(refId=refId,password=password)
        user.save()
        print("sjhdhdbvjhdahvb")
        print(graphene.Field(UserType))
        return createUser(user=user,ok=True)
        # return createUser( ok=True)
    
class Mutation(graphene.ObjectType):
    create_User = createUser.Field()