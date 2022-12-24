from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import ( AbstractUser)


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, refId, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not refId:
            raise ValueError(('The Email must be set'))
        refId = self.normalize_email(refId)
        user = self.model(refId=refId, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, refId, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(refId, password, **extra_fields)

class UserModel(AbstractUser):
    username = None
    last_login = None
    date_joined = None
    email = None
    refId = models.EmailField(unique=True, max_length=254)
    ex = models.TextField(max_length=200, blank=True, null=True)
    USERNAME_FIELD = 'refId'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
