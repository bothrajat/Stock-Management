from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from management.models import *

# Create your views here.


def home(request):
    return redirect("order-booking")


def order_booking(request):
    if request.method=='POST':
        CustomerName=request.POST.get('CustomerName')
        Date=request.POST.get('Date')
        OrderNo=int(request.POST.get('OrderNo'))
        Colour=request.POST.get('Colour')
        Quality=request.POST.get('Quality')
        OrderedQuantity=int(request.POST.get('OrderedQuantity'))
        BalanceQuantity=int(request.POST.get('BalanceQuantity'))
        Order_obj=Order()
        Order_obj.CustomerName=Customer.objects.get(CustomerName=CustomerName)
        Order_obj.Date=Date
        Order_obj.OrderNo=OrderNo
        Order_obj.Colour=Colour.objects.get(Colour=Colour)
        Order_obj.Quality=Quality.objects.get(Quality=Quality)
        Order_obj.OrderedQuantity=OrderedQuantity
        Order_obj.BalanceQuantity=BalanceQuantity
        Order_obj.save()
        return
    return render(request, "order_booking.html",context={'SerialNo':Order.objects.count()+1})


def stock_view(request):
    return render(request, "stock-view.html")


def consumption_record(request):
    return render(request, "consumption-record.html")


def stock_movement(request):
    return render(request, "stock-movement.html")


def production_input(request):
    return render(request, "production-input.html")
