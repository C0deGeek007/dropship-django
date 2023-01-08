from django.urls import path

from . import views
from graphene_django.views import GraphQLView
# from .schema import schema
from django.views.decorators.csrf import csrf_exempt
from .graphql.schema import schema

urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register, name="add-user"),
    path('login', views.login, name="login-user"),
    path('logout', views.logout, name="logout-user"),
    path('users', views.users, name="get-all-user"),
    path("users-graphql", csrf_exempt(views.PrivateGraphQLView.as_view(graphiql=True, schema = schema ))),
]