from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from management.models import *
import json, ast

# Create your views here.
def home(request):
    return redirect("order-booking")


def collect(request):
    OrderList = request.POST.get("OrderList")
    ID = request.POST.get("ID")
    if not OrderList:
        OrderList = {}
        ID = 1
    else:
        OrderList = ast.literal_eval(OrderList)
        if not ID:
            ID = max(OrderList.keys()) + 1
        else:
            ID = int(ID)
    return {
        "SerialNo": int(request.POST.get("SerialNo")),
        "OrderNo": request.POST.get("OrderNo"),
        "Date": request.POST.get("Date"),
        "CustomerName": request.POST.get("CustomerName"),
        "Quality": request.POST.get("Quality"),
        "Colour": request.POST.get("Colour"),
        "Quantity": int(request.POST.get("Quantity", 0)),
        "OrderList": OrderList,
        "ID": ID,
    }


def order_booking(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Customers = Customer.objects.all()
    SerialNo = Order.objects.count() + 1
    if request.method == "POST":
        data = collect(request)

        if request.POST.get("save"):
            data["OrderList"][data["ID"]] = {
                "Quality": data["Quality"],
                "Colour": data["Colour"],
                "Quantity": data["Quantity"],
            }

        elif request.POST.get("remove"):
            pass
        elif request.POST.get("submit"):
            pass
        return render(
            request,
            "order_booking.html",
            context={
                **data,
                "Colours": Colours,
                "Qualities": Qualities,
                "Customers": Customers,
            },
        )
    return render(
        request,
        "order_booking.html",
        context={
            "SerialNo": SerialNo,
            "Colours": Colours,
            "Qualities": Qualities,
            "Customers": Customers,
        },
    )


def stock_view(request):
    return render(request, "stock-view.html")


def consumption_record(request):
    return render(request, "consumption-record.html")


def stock_movement(request):
    return render(request, "stock-movement.html")


def production_input(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    if request.method =="POST":
        if request.POST.get("submit"):
            data[FactoryStock][data[ID]]={
                
            }


    return render(request, "production-input.html")
