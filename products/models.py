from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    # New fields
    discount = models.BooleanField(default=False)
    discount_percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def selling_price(self):
        """Calculated price after discount"""
        if self.discount and 0 <= self.discount_percentage <= 100:
            return self.price * (1 - self.discount_percentage / 100)
        return self.price