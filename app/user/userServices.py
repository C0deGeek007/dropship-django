from django.contrib.auth import get_user_model
from .userSerializer import UserSerializers, loginSerializer, loginResponseSerializer
from django.contrib.auth.hashers import check_password
from .exceptions import userDoesNotExist,wrongPassword
import jwt

class UserService:

    @classmethod
    def loginUser(cls, **credentials):
        print("inside login user service")
        # print(get_user_model().check_password( raw_password= credentials['password']))
        try:
            user = get_user_model().objects.get(refId=credentials['refId'])
            if(check_password(credentials['password'], UserSerializers(user).data['password'])):
                print(loginSerializer(user).data)
                return UserService.tokenGeneration(**loginResponseSerializer(user).data)
                # return loginResponseSerializer(user).data
            else:
                raise wrongPassword()
            # print(check_password(credentials['password'], UserSerializers(user).data['password']))
        except get_user_model().DoesNotExist as e:
            raise userDoesNotExist()

    @classmethod
    def tokenGeneration(cls, **userInfo):
        print("inside token generation")
        print(userInfo)
        return jwt.encode({"userInfo": userInfo }, "secret1ForThisProject", algorithm="HS256")