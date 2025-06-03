from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    shop = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    picture = models.URLField(blank=True, null=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

