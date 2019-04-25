from django.urls import path
from .views import InvoiceDetailView
from . import views

urlpatterns = [
    path('home/', views.home, name='refurbco-home'),
    path('inventory/', views.inventory, name='refurbco-inventory'),
    path('invoices/', views.invoices, name='refurbco-invoices'),
    path('login/', views.login, name='refurbco-login'),
    path('metrics/', views.metrics, name='refurbco-metrics'),
    path('pricechecker/', views.priceChecker, name='refurbco-pricechecker'),
    path('repairs/', views.repairs, name='refurbco-repairs'),
    path('account/', views.account, name='refurbco-account'),
    path('inventory/addOrder/', views.addOrder, name='refurbco-addOrder'),

    path('refurbco/invoice/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail')
]