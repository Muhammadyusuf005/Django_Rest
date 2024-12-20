from django.db import models

from django.contrib.auth.models import AbstractBaseUser, AbstractUser

from myapp.base import BaseModel


class Account(AbstractUser,BaseModel):
    """
    Main User Model for this project!
    """

    REQUIRED_FIELDS = ['first_name', 'last_name']
