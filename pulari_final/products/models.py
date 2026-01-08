
# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255) # Pipe Name
    category = models.CharField(max_length=100) # PVC, CPVC, etc.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pipes_images/') # Image store panna

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    product = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.product})"
