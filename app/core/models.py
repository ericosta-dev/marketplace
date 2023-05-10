from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models

class UserManager(DefaultUserManager):
    pass

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15)

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    is_primary = models.BooleanField(default=False)
