from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    pass

    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password1'
    EMAIL_FIELD = 'email'


