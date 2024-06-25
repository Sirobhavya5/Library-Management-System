import uuid
from django.db import models

from users.models import CustomUser

# Create your models here.
class Library(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    owner = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
