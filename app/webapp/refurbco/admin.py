from django.contrib import admin
from .models import RepairTicket, Order, Inventory, Repair, Invoice

# Register your models here.

admin.site.register(RepairTicket)
admin.site.register(Order)
admin.site.register(Inventory)
admin.site.register(Repair)
admin.site.register(Invoice)