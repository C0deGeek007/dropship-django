import jwt
from django.contrib.auth import get_user_model
# from rest_framework import authentication
# from rest_framework import exceptions
# from rest_framework.authentication import get_authorization_header
from django.conf import settings
from django.contrib.auth.backends import BaseBackend

class ExampleAuthentication(BaseBackend):
    def authenticate(self, request):    
        print(request.data)
        print("inside authentication backend")
        print(request.headers.get('Authorization').split(' ')[1])
        token = request.headers.get('Authorization').split(' ')[1]
        try:
            decode = jwt.decode(token, "secret1ForThisProject", algorithms=["HS256"])
            print(decode)
            user = get_user_model().objects.get(refId=decode['userInfo']['refId'])
            request.user = user
            print(user)
        except (get_user_model().DoesNotExist, jwt.exceptions.InvalidSignatureError):
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)
    
    def get_user(self, user_id):
        print("inside get user auth backend")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None