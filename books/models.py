import uuid
from django.db import models

from users.models import CustomUser
from libraries.models import Library
from authors.models import Author
from publishers.models import Publisher
from vendors.models import Vendor

# Create your models here.
class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=4)
    library = models.ForeignKey(to=Library, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, default=None)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, default=None)
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE, default=None)

    status = models.CharField(max_length=255)
    borrower = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, default=None, null=True)
    borrow_date = models.DateField(default=None, null=True)
    return_date = models.DateField(default=None, null=True)
    charge = models.DecimalField(max_digits=6, decimal_places=4)
