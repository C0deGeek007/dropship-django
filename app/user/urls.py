from django.urls import path

from . import views
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register, name="add-user"),
    path('login', views.login, name="login-user"),
    path('users', views.users, name="get-all-user"),
    path("users-graphql", views.PrivateGraphQLView.as_view(graphiql=True, schema = schema )),
]