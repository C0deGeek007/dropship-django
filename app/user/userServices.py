from django.contrib.auth import get_user_model
from .userSerializer import UserSerializers, loginSerializer, loginResponseSerializer
from django.contrib.auth.hashers import check_password
from .exceptions import userDoesNotExist,wrongPassword
import jwt
from django.contrib.auth import login, logout
import json

class UserService:

    @classmethod
    def loginUser(cls,request, **credentials):
        try:
            user = get_user_model().objects.get(refId=credentials['refId'])
            if(check_password(credentials['password'], UserSerializers(user).data['password'])):
                print(json.dumps(dir(request)))
                login(request, user)
                print(json.dumps(dir(request)))
                return UserService.tokenGeneration(**loginResponseSerializer(user).data)
                # return loginResponseSerializer(user).data
            else:
                raise wrongPassword()
            # print(check_password(credentials['password'], UserSerializers(user).data['password']))
        except get_user_model().DoesNotExist as e:
            raise userDoesNotExist()

    @classmethod
    def tokenGeneration(cls, **userInfo):
        return jwt.encode({"userInfo": userInfo }, "secret1ForThisProject", algorithm="HS256")
    
    @classmethod
    def logoutUser(cls, request):
        return logout(request)