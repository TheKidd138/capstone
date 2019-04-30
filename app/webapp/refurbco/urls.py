from django.urls import path
from .views import ViewInvoice, ViewPart, ViewRepairTicket, ViewRepair
from . import views

urlpatterns = [
    path('home/', views.home, name='refurbco-home'),
    path('inventory/', views.inventory, name='refurbco-inventory'),
    path('inventory/<int:pk>/', ViewPart.as_view(), name='refurbco-viewPart'),
    path('inventory/updatepart/', views.updatePart, name='refurbco-updatePart'),
    path('inventory/updatepart/updatePartFinalize', views.updatePartFinalize, name='refurbco-updatePartFinalize'),
    path('inventory/addOrder/', views.addOrder, name='refurbco-addOrder'),
    path('inventory/addOrder/addPart', views.addPart, name='refurbco-addPart'),
    path('inventory/addOrder/addPart/finishOrder', views.finishOrder, name='refurbco-finishOrder'),
    path('repairtickets/', views.repairTickets, name='refurbco-repairTickets'),
    path('repairtickets/<int:pk>/', ViewRepairTicket.as_view(), name='refurbco-viewRepairTicket'),
    path('repairtickets/update/', views.updateRepairTicket, name='refurbco-updateRepairTicket'),
    path('repairtickets/update/updatefinalize', views.updateRepairTicketFinalize, name='refurbco-updateRepairTicketFinalize'),
    path('repairtickets/createrepairticket/', views.createRepairTicket, name='refurbco-createRepairTicket'),
    path('repairtickets/createrepairticket/addrepairticket', views.addRepairTicket, name='refurbco-addRepairTicket'),
    path('repairs/', views.repairs, name='refurbco-repairs'),
    path('repairs/<int:pk>/', ViewRepair.as_view(), name='refurbco-viewRepair'),
    path('repairs/update/', views.updateRepair, name='refurbco-updateRepair'),
    path('repairs/update/updaterepairfinalize', views.updateRepairFinalize, name='refurbco-updateRepairFinalize'),
    path('repairs/completerepair/', views.completeRepair, name='refurbco-completeRepair'),
    path('repairs/completerepair/processrepair', views.processRepair, name='refurbco-processRepair'),    
    path('invoices/', views.invoices, name='refurbco-invoices'),
    path('invoice/<int:pk>/', ViewInvoice.as_view(), name='refurbco-viewInvoice'),
    path('invoices/generateinvoices/', views.generateInvoices, name='refurbco-generateInvoices'),
    #path('login/', views.login, name='refurbco-login'),
    #path('metrics/', views.metrics, name='refurbco-metrics'),
    #path('generatequote/', views.generateQuote, name='refurbco-quote'),
    #path('generatequote/createQuote/', views.createQuote, name='refurbco-createQuote'),
    #path('account/', views.account, name='refurbco-account'),
    

    
]