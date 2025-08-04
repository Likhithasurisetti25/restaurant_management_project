from django.db import models
from django.contrib.auth.models import User
from products.models import Menu
cladd Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('DELIVERD','Delivered'),
        ('CANCELLED','Cancelled'),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.Many_To_ManyField(Menu)
    total_amount=models.DecimalField(max_digit=8,decimal_places=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
# Create your models here.
