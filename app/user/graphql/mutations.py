import graphene
from django.contrib.auth import get_user_model
from .type import UserType
from django.template import loader
import pdfkit

# https://en.wikipedia.org/wiki/Pel%C3%A9


class createUser(graphene.Mutation):
    
    user =  graphene.Field(lambda:UserType)
    ok = graphene.Boolean()
    
    class Arguments:
        refId = graphene.String()
        password = graphene.String()
    
    def mutate(root, info, refId, password):
        user = get_user_model().objects.create_user(refId=refId,password=password)
        # user = UserType(refId=refId,password=password)
        # print(loader.render_to_string("index.html"))
        try:
            render = loader.render_to_string("user/index.html", {'refId':refId})
            print(render)
            pdf = pdfkit.from_string(render,"out.pdf")
            print(pdf)
        except:
            print("something went wrong")
        
        user.save()
        print("sjhdhdbvjhdahvb")
        print(graphene.Field(UserType))
        return createUser(user=user,ok=True)
        # return createUser( ok=True)
    
class Mutation(graphene.ObjectType):
    create_User = createUser.Field()