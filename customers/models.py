from django.db import models


# class ExtendUser(AbstractUser):
#     pass
#
#     USERNAME_FIELD = 'username'
#     PASSWORD_FIELD = 'password1'
#     EMAIL_FIELD = 'email'

class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime('%d/%m/%Y - %H:%M')

    def get_updated_at(self):
        return self.updated_at.strftime('%d/%m/%Y - %H:%M')

    class Meta:
        verbose_name_plural = 'Users'


