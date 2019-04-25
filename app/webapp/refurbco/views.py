from django.shortcuts import render
from django.views.generic import DetailView
from .models import Invoice, Inventory, Device, PartType
#from .models import [class]

# Create your views here.



def home(request):
  return render(request, 'refurbco/home.html', {'title':'Home'})

def inventory(request):
  context = {
    'inventory': Inventory.objects.all(),
    'deviceList': Device.objects.all()
  }
  return render(request, 'refurbco/inventory.html', context)

def invoices(request):
  context = {
    'title':'Invoices',
    'invoices': Invoice.objects.all()
  }
  return render(request, 'refurbco/invoices.html', context)

def login(request):
  return render(request, 'refurbco/login.html', {'title':'Login'})

def metrics(request):
  return render(request, 'refurbco/metrics.html', {'title':'Metrics'})

def priceChecker(request):
  return render(request, 'refurbco/priceChecker.html', {'title':'Price Checker'})

def repairs(request):
  return render(request, 'refurbco/repairs.html', {'title':'Repairs'})

def account(request):
  return render(request, 'refurbco/account.html', {'title':'Account'})

def addOrder(request):
  context = {
    'title':'Add Order',
    'parts': PartType.objects.all()
  }
  return render(request, 'refurbco/addOrder.html', context)

class InvoiceDetailView(DetailView):
  model = Invoice
  