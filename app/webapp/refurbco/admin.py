from django.contrib import admin
from .models import RepairTicket, Order, Inventory, Repair, Invoice, Device, PartType

# Register your models here.

admin.site.register(RepairTicket)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Repair)
admin.site.register(Invoice)
admin.site.register(Device)
admin.site.register(PartType)