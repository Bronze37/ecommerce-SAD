from django.db import models

from order.models import Order

class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100, unique=True)
    carrier = models.CharField(max_length=100)
    estimated_delivery = models.DateField()