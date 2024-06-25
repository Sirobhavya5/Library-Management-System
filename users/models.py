import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from users.managers import CustomUserManager

ROLE_CHOICES =(
    ("1", "member"),
    ("2", "employee"),
    ("3", "owner")
)
  
class CustomUser(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default="1")
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
