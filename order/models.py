from django.db import models

from customer.models import Customer

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')])
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=24)  # Lưu ObjectId của MongoDB dưới dạng chuỗi
    product_type = models.CharField(max_length=10, choices=[
        ('book', 'Book'),
        ('mobile', 'Mobile'),
        ('clothes', 'Clothes')
    ])
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Lưu giá tại thời điểm đặt hàng
