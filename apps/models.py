from django.db import models
from django.db.models import DateTimeField, TextChoices


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='menu_items/')
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    # link_text = models.CharField(max_length=255, blank=True, null=True)
    # link_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    class Type(TextChoices):
        NEW = 'new', 'NEW'
        PENDING = 'pending', 'PENDING'
        CANCELED = 'canceled', 'CANCELED'
        DELIVERED = 'delivered', 'DELIVERED'

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    product_detail = models.CharField(max_length=1000)
    booking_date = DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=Type.choices, default=Type.NEW)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True, blank=True, related_name='products')

    def __str__(self):
        return f"{self.name} on {self.status}"
