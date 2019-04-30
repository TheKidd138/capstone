from django.db import models
from django.utils import timezone

# Create your models here.


class RepairTicket(models.Model):
    #ID = models.AutoField(primary_key=True)
    model_number = models.TextField(max_length=5)
    issue = models.TextField(max_length=500, blank=True)
    serial_number = models.TextField(max_length=12)
    device_owner = models.TextField(max_length=20)
    ticket_number = models.TextField(max_length=5, blank=True)
    charged = models.TextField(max_length=20, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Device(models.Model):
    #ID = models.AutoField(primary_key=True)
    model_number = models.TextField(max_length=5)
    device_type = models.TextField(max_length=16)

    def __str__(self):
        return self.device_type
    
    def device(self):
        return self.device_type

class PartType(models.Model):
    #ID = models.AutoField(primary_key=True)
    mdap = models.TextField(max_length=8)
    part_type = models.TextField(max_length=16)
    quoteCost = models.TextField(max_length=10, blank=True)

    def __str__(self):
        return str(self.id)

    def part(self):
        return self.part_type

class Order(models.Model):
    #ID = models.AutoField(primary_key=True)
    order_number = models.TextField(max_length=20) #
    order_size = models.TextField(max_length=20)
    subtotal = models.TextField(max_length=20) #models.DecimalField(max_digits=4, decimal_places=2)
    shipping = models.TextField(max_length=20) #models.DecimalField(max_digits=4, decimal_places=2)
    total = models.TextField(max_length=20) #models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.order_number

    

class Inventory(models.Model):
    #ID = models.AutoField(primary_key=True)
    mdap = models.TextField(max_length=8, blank=True)
    part = models.TextField(max_length=20) #models.ForeignKey(PartType, on_delete=models.PROTECT)
    device = models.TextField(max_length=20) #models.ForeignKey(Device, on_delete=models.PROTECT)
    order = models.TextField(max_length=20) #models.ForeignKey(Order, on_delete=models.PROTECT)
    part_cost = models.DecimalField(max_digits=4, decimal_places=2)
    color = models.TextField(max_length=12, blank=True) #

    def __str__(self):
        return str(self.id)

class Repair(models.Model):
    #ID = models.AutoField(primary_key=True)
    repairticket = models.ForeignKey(RepairTicket, on_delete=models.PROTECT)
    repair_notes = models.TextField(max_length=500)
    part_used = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    repaired_on = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)

class Invoice(models.Model):

    paymentMethods = (('check', 'Check'), ('cash', 'Cash'))

    #ID = models.AutoField(primary_key=True)
    repairticket = models.ForeignKey(RepairTicket, on_delete=models.PROTECT)
    repair = models.ForeignKey(Repair, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=timezone.now)
    charged = models.TextField(max_length=20)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=5, choices=paymentMethods, default='check')

    def __stf__(self):
        return self.id





#class Quote(models.Model):


