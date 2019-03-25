from django.shortcuts import render
#from .models import [class]

# Create your views here.



def home(request):
  return render(request, 'refurbco/home.html', {'title':'Home'})

def inventory(request):
  context = {
#    'parts': Part.objects.all()
    'title':'Inventory'
  }
  return render(request, 'refurbco/inventory.html', context)

def invoices(request):
  return render(request, 'refurbco/invoices.html', {'title':'Invoices'})

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