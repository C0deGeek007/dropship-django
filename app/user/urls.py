from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register, name="add-user"),
    path('login', views.login, name="login-user"),
    path('users', views.users, name="get-all-user")
]