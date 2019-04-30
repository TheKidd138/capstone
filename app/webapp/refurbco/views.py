from django.shortcuts import render
from django.http import request, response
from django.views.generic import DetailView
from .models import Invoice, Inventory, Device, PartType, Order, Repair, RepairTicket
#from .models import [class]

# Create your views here.



def home(request):
  print('Howdy Server')

  repairTickets = RepairTicket.objects.filter(completed=True)
  repairs = Repair.objects.filter(complete=True)
  invoices = Invoice.objects.filter(paid=False)
  order = Order.objects.last()

  context = {
      'title':'Home',
      'repairTicketsPending': len(repairTickets),
      'repairsInProgress': len(repairs),
      'invoicesOutstanding': len(invoices),
      'previousOrder': order.order_number
    }

  return render(request, 'refurbco/home.html', context)

def inventory(request):
  context = {
    'title':'Inventory',
    'inventory': Inventory.objects.all(),
    'deviceList': Device.objects.all()
  }
  return render(request, 'refurbco/inventory.html', context)

class ViewPart(DetailView):
  model = Inventory

def updatePart(request):
  if request.method == 'POST':

    partID = request.POST.get('partID')
    part = Inventory.objects.filter(id=partID)

  context = {
    'title': 'Update Inventory',
    'part': part[0],
    'deviceList': Device.objects.all()
  }
  return render(request, 'refurbco/updateinventory.html', context)

def updatePartFinalize(request):
  if request.method=='POST':

    partID = request.POST.get('partID')
    mdap = str(request.POST.get('mdap'))
    deviceType = str(request.POST.get('deviceType'))
    price = str(request.POST.get('price'))

    updatePartInDB(partID, mdap, deviceType, price)

  context = {
    'title':'Inventory',
    'inventory': Inventory.objects.all(),
    'deviceList': Device.objects.all()
  }
  return render(request, 'refurbco/inventory.html', context)

def addOrder(request):
  
  context = {
    'title':'Add Order',
    'parts': PartType.objects.all()
  }
  return render(request, 'refurbco/addOrder.html', context)

def addPart(request):
  if request.method=='POST':
    
    orderNumber = str(request.POST.get('orderNumber'))
    quantity = str(request.POST.get('quantity'))
    shipping = str(request.POST.get('shipping'))
    subtotal = str(request.POST.get('subtotal'))
    total=(shipping+subtotal)

    if (Order.objects.filter(order_number=orderNumber).exists()):
      context = {
        'title':'Add Order',
        'deviceList': Device.objects.all(),
        'error': 'Order already exists'
      }
      return render(request, 'refurbco/addOrder.html', context)
    else:
      order = Order(order_number=orderNumber, order_size=quantity,
        subtotal=subtotal, shipping=shipping, total=total)
      order.save()

  context = {
    'title':'Add Part',
    'deviceList': Device.objects.all(),
    'order':Order.objects.filter(order_number=orderNumber)
  }
  
  return render(request, 'refurbco/addPart.html', context)

def finishOrder(request):
  if request.method=='POST':
    orderNumber = str(request.POST.get('orderNumber'))
    mdap = str(request.POST.get('mdap'))
    price = str(request.POST.get('price'))
    device = str(request.POST.get('deviceType'))
    orderStatus = str(request.POST.get('status'))

    if(orderStatus == 'Finish Order'):
      addPartToDB(orderNumber, mdap, device, price)
      return inventory(request)
    elif(orderStatus == 'Add Another Part'):
      addPartToDB(orderNumber, mdap, device, price)
      context = {
        'title':'Add Part',
        'order':Order.objects.filter(order_number=orderNumber)
      }
      return render(request, 'refurbco/addPart.html', context)


def repairTickets(request):
  context = {
    'title':'Invoices',
    'repairs': RepairTicket.objects.all()
  }

  return render(request, 'refurbco/repairticket.html', context)

class ViewRepairTicket(DetailView):
  model = RepairTicket

def createRepairTicket(request):
  context = {
    'title':'Create Repair Ticket'
  }
  return render(request, 'refurbco/createrepairticket.html', context)

def updateRepairTicket(request):

  TicketID = request.POST.get('repairTicketID')
  repairTicket = RepairTicket.objects.filter(id=TicketID)

  context = {
    'title': 'Update Repair Ticket',
    'repairTicket': repairTicket[0]
  }
  return render(request, 'refurbco/updaterepairticket.html', context)

def updateRepairTicketFinalize(request):
  if request.method=='POST':
    repairTicketID = request.POST.get('repairTicketID')
    modelNumber = str(request.POST.get('modelNumber'))
    issue = str(request.POST.get('issue'))
    serial = str(request.POST.get('serial'))
    owner = str(request.POST.get('owner'))
    ticket = str(request.POST.get('ticket'))
    charged = str(request.POST.get('charged'))
    status = str(request.POST.get('status'))

    updateRepairTicketToDB(repairTicketID, modelNumber, issue, serial, owner, ticket, charged, status)

  context = {
    'title':'Invoices',
    'repairs': RepairTicket.objects.all()
  }

  return render(request, 'refurbco/repairticket.html', context)

def addRepairTicket(request):
  if request.method=='POST':
    modelNumber = str(request.POST.get('modelNumber'))
    issue = str(request.POST.get('issue'))
    serialNumber = str(request.POST.get('serial'))
    deviceOwner = str(request.POST.get('owner'))
    ticketNumber = str(request.POST.get('ticket'))
    charged = str(request.POST.get('charged'))

    addRepairTicketToDB(modelNumber, issue, serialNumber, deviceOwner, ticketNumber, charged)

  return repairTickets(request)

def repairs(request):
  context = {
    'title':'Invoices',
    'repairs': Repair.objects.all()
  }

  return render(request, 'refurbco/repairs.html', context)

class ViewRepair(DetailView):
  model = Repair

def updateRepair(request):

  repairID = request.POST.get('repairID')
  repair = Repair.objects.filter(id=repairID)

  context = {
      'title': 'Update Repair',
      'repair': repair[0],
      'repairTickets': RepairTicket.objects.all(),
      'parts': Inventory.objects.all()
    }
  return render(request, 'refurbco/updaterepair.html', context)

def updateRepairFinalize(request):

  if request.method=='POST':

    repairID = request.POST.get('repairID')

    repairticketID = request.POST.get('repairTicket')
    repairticket = RepairTicket.objects.filter(id=repairticketID)

    issue = str(request.POST.get('issue'))

    partUsedID = request.POST.get('partUsed')
    partUsed = Inventory.objects.filter(id=partUsedID)
  
    complete = str(request.POST.get('status'))
    
    updateRepairToDB(repairID, repairticket[0], issue, partUsed[0], complete)

  context = {
    'title':'Invoices',
    'repairs': Repair.objects.all()
  }
  return render(request, 'refurbco/repairs.html', context)

def completeRepair(request):
  context = {
    'title':'Complete a Repair',
    'repairTickets': RepairTicket.objects.all(),
    'parts': Inventory.objects.all()
  }

  return render(request, 'refurbco/completerepair.html', context)

def processRepair(request):
  if request.method=='POST':
    repairTicket = request.POST.get('repairTicket')
    notes = str(request.POST.get('notes'))
    partUsed = request.POST.get('partUsed')
    print(repairTicket)
    print(partUsed)

    repairTicketInstance = RepairTicket.objects.filter(id=repairTicket)
    partUsedInstance = Inventory.objects.filter(mdap=partUsed)

    addRepairToDB(repairTicketInstance[0], notes, partUsedInstance[0])

  return repairs(request)

def invoices(request):
  context = {
    'title':'Invoices',
    'invoices': Invoice.objects.all()
  }
  return render(request, 'refurbco/invoices.html', context)

class ViewInvoice(DetailView):
  model = Invoice

def generateInvoices(request):
  unfulfilled = []
  invoices = Invoice.objects.all()
  invoicesToRepairs = []
  for invoice in invoices:
    invoicesToRepairs.append(invoice.repairticket)

  repairs = Repair.objects.filter(complete=True)
  if len(repairs) > len(invoicesToRepairs):
    for repair in repairs:
      if repair.repairticket not in invoicesToRepairs:
        unfulfilled.append(repair)
  if len(unfulfilled)> 0:
    createInvoice(unfulfilled, repairs)
  del unfulfilled, invoices, invoicesToRepairs

  context = {
    'title':'Generate Invoices',
    'invoices': Invoice.objects.all()
  }
  return render(request, 'refurbco/invoices.html', context)


def addPartToDB(orderNumber, mdap, device, price):
  part = Inventory(mdap=mdap, part=PartType.objects.filter(mdap=mdap)[0].part(), device=device, order=orderNumber, part_cost=price)
  part.save()

def updatePartInDB(part, mdap, deviceType, price):
  inv = Inventory.objects.filter(id=part)[0]
  inv.mdap = mdap
  inv.part = PartType.objects.filter(mdap=mdap)[0].part()
  inv.device = deviceType
  inv.part_cost = price
  inv.save()

def addRepairTicketToDB(modelNumber, issue, serialNumber, deviceOwner, ticketnumber, charged):
  ticket = RepairTicket(model_number=modelNumber, issue=issue, serial_number=serialNumber, device_owner=deviceOwner, ticket_number=ticketnumber, charged=charged)
  ticket.save()

def updateRepairTicketToDB(repairTicketID, modelNumber, issue, serial, owner, ticket, charged, status):
  tic = RepairTicket.objects.filter(id=repairTicketID)[0]
  tic.model_number = modelNumber
  tic.issue = issue
  tic.serial_number = serial
  tic.device_owner = owner
  tic.ticket_number = ticket
  tic.charged = charged
  tic.completed = status
  tic.save()

def addRepairToDB(repairTicket, notes, partUsed):
  repair = Repair(repairticket=repairTicket, repair_notes=notes, part_used=partUsed, complete=True)
  repair.save()

def updateRepairToDB(repairID, repairticket, issue, partUsed, complete):
  rep = Repair.objects.filter(id=repairID)[0]
  rep.repairticket = repairticket
  rep.repair_notes = issue
  rep.part_used = partUsed
  rep.complete = complete
  rep.save()

def createInvoice(unfulfilled, repair):
  for i in unfulfilled:
    invoice = Invoice(repairticket=i.repairticket, repair=i, charged=i.repairticket.charged)
    invoice.save()


  

#def generateQuote(request):

#context = {
#  'title':'Generate Quote',
#  'deviceList': Device.objects.all(),
#  'partList': PartType.objects.all(),
#}
#return render(request, 'refurbco/generatequote.html', context)

#def createQuote(request):

#context = {
#  {'title':'Generate Quote'}
#}
#return render(request, 'refurbco/home.html', context)
#def login(request):
#  return render(request, 'refurbco/login.html', {'title':'Login'})

#def metrics(request):
#  return render(request, 'refurbco/metrics.html', {'title':'Metrics'})

#def account(request):
#  return render(request, 'refurbco/account.html', {'title':'Account'})