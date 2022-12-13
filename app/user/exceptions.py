from rest_framework.exceptions import APIException


class userDoesNotExist(APIException):
    status_code = 404
    default_detail = "User Does Not Exist"

class wrongPassword(APIException):
    status_code = 401
    default_detail = "Wrong Password"