from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .userSerializer import UserSerializers, loginSerializer
from .userServices import UserService
from .authBackend import ExampleAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import AccessMixin
from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin


@api_view(['POST'])
def register(request):
    serializer = UserSerializers(data=request.data)
    print(request.user)
    if(serializer.is_valid(raise_exception=True)):
        res = UserSerializers.create(serializer.validated_data)
        print(UserSerializers(res).data)
        return Response(UserSerializers(res).data)
        print(res.id)
    return Response("error")

@api_view(['POST'])
def login(request):
    serializer = loginSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        res = UserService.loginUser(**serializer.data)
        return Response({"token":res,"status": 201}, status=201)
        # print(serializer.validated_data)
    return Response("inside login view")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
    # ExampleAuthentication().authenticate(request)
    print("inside users view")
    print(UserSerializers(request.user).data)
    return Response("inside get all user")

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass