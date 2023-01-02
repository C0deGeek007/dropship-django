import graphene
from django.contrib.auth import get_user_model
from .userType import UserType

class createUserMutation(graphene.Mutation):
    class Arguments:
        refId = graphene.String()
        password = graphene.String()
        
    res =  graphene.Field(UserType)
    
    def mutate(self,refId,password):
        user = get_user_model().objects.create(refId=refId,password=password)
        user.save()
        print("sjhdhdbvjhdahvb")
        return createUserMutation(user)