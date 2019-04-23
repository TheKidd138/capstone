from django.db import models
from django.utils import timezone

# Create your models here.


class RepairTicket(models.Model):
    model_number = models.TextField(max_length=4)
    issue = models.TextField(max_length=500)
    serial_number = models.TextField(max_length=12)
    device_owner = models.TextField()
    ticket_number = models.TextField(max_length=5)
    comments = models.TextField(max_length=500)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ticket_number

class Device(models.Model):
    model_number = models.TextField(max_length=5)
    device = models.TextField(max_length=16)

    def __str__(self):
        return self.device

class PartType(models.Model):
    mdap = models.TextField(max_length=8)
    part_type = models.TextField(max_length=16)
    quoteCost = models.TextField(max_length=10)

    def __str__(self):
        return self.part_type

class Order(models.Model):
    order_number = models.TextField(max_length=20)
    order_size = models.PositiveIntegerField()
    subtotal = models.TextField(max_length=10)
    shipping = models.TextField(max_length=10)
    total = models.TextField(max_length=10)

    def __str__(self):
        return self.order_number

class Inventory(models.Model):
    mdap = models.TextField(max_length=8)
    part_type = models.ForeignKey(PartType, on_delete=models.PROTECT)
    device_type = models.ForeignKey(Device, on_delete=models.PROTECT)
    order_number = models.ForeignKey(Order, on_delete=models.PROTECT)
    part_cost = models.TextField(max_length=10)
    color = models.CharField(max_length=12)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.part_type

class Repair(models.Model):
    repairticket = models.OneToOneField(RepairTicket, on_delete=models.PROTECT)
    repair_notes = models.TextField(max_length=500)
    part_used = models.OneToOneField(Inventory, on_delete=models.PROTECT)
    repaired_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.repairticket

class Invoice(models.Model):
    repairticket = models.OneToOneField(RepairTicket, on_delete=models.PROTECT)
    repair = models.OneToOneField(Repair, on_delete=models.PROTECT)
    received_on = models.DateTimeField()
    repaired_on = models.DateTimeField()  
    returned_on = models.DateTimeField(default=timezone.now)
    charged = models.TextField(max_length=10)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=6)

    def __stf__(self):
        return 'ID'





#class Quote(models.Model):


