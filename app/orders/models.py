from django.db import models
from app.core.models import Address
from app.core.models import CustomUser
from app.cart.models import ShoppingCart
from app.payment.models import PaymentMethod


class Order(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processed", "Processed"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
