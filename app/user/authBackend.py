import jwt
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.data)
        print("inside authentication backend")
        print(request.headers.get('Authorization').split(' ')[1])
        token = request.headers.get('Authorization').split(' ')[1]
        try:
            decode = jwt.decode(token, "secret1ForThisProject", algorithms=["HS256"])
            print(decode)
            user = get_user_model().objects.get(refId=decode['userInfo']['refId'])
            print(user)
        except (get_user_model().DoesNotExist, jwt.exceptions.InvalidSignatureError):
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)