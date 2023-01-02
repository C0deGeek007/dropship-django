from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        # fields = ["refId","password","id"]
        fields = "__all__"