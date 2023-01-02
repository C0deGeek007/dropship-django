from .type import UserType
import graphene
from django.contrib.auth import get_user_model
from rest_framework.response import Response

class Query(graphene.ObjectType):
    allUser = graphene.List(UserType)
    def resolve_allUser(root,info):
        info = get_user_model().objects.all()        
        print(info)
        print("inside new query")
        return info
        # return Response(info)