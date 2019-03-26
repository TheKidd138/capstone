from django.db import models
from django.utils import timezone

# Create your models here.


class RepairTicket(models.Model):
    model_number = models.PositiveIntegerField(max_length=4)
    issue = models.TextField(max_length=500)
    serial_number = models.TextField(max_length=12)
    device_owner = models.TextField()
    ticket_number = models.PositiveIntegerField(max_length=6)
    comments = models.TextField(max_length=500)
    created_on = models.DateTimeField(default=timezone.now)

class Repair(models.Model):
    repair_ticket_ID = models.OneToOneField(RepairTicket)
    repair_notes = models.TextField(max_length=500)
    parts_used = models.CommaSeparatedIntegerField()
    repaired_on = models.DateTimeField(default=timezone.now)

class Inventory(models.Model):
    order_number = models.IntegerField(max_length=20)
    part_cost = models.TextField(max_length=10)
    device_type = models.CharField(max_length=12)
    part_type = models.CharField(max_length=18)
    color = models.CharField(max_length=12)
    used = models.BooleanField(default=False)

#class Invoice(models.Model):


#class Order(models.Model):


#class Quote(models.Model):


