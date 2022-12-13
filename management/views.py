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
    Quantity = request.POST.get("Quantity")
    if Quantity:
        Quantity = int(Quantity)
    else:
        Quantity = 0
    if OrderList and OrderList != "{}":
        OrderList = ast.literal_eval(OrderList)
        if not ID:
            ID = max(OrderList.keys()) + 1
        else:
            ID = int(ID)
    else:
        OrderList = {}
        ID = 1
    return {
        "SerialNo": int(request.POST.get("SerialNo")),
        "OrderNo": int(request.POST.get("OrderNo")),
        "Date": request.POST.get("Date"),
        "CustomerName": request.POST.get("CustomerName"),
        "Quality": request.POST.get("Quality"),
        "Colour": request.POST.get("Colour"),
        "Quantity": Quantity,
        "OrderList": OrderList,
        "ID": ID,
    }


def order_booking(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Customers = Customer.objects.all()
    SerialNo = Order.objects.count() + 1
    context = {
        "SerialNo": SerialNo,
        "Colours": Colours,
        "Qualities": Qualities,
        "Customers": Customers,
    }
    if request.method == "POST":
        data = collect(request)

        if request.POST.get("save"):
            data["OrderList"][data["ID"]] = {
                "Quality": data["Quality"],
                "Colour": data["Colour"],
                "Quantity": data["Quantity"],
            }

        elif request.POST.get("remove"):
            del data["OrderList"][data["ID"]]

        elif request.POST.get("submit"):
            order = Order.objects.create(OrderNo=data["OrderNo"])
            customer = Customer.objects.get(CustomerName=data["CustomerName"])
            Date = data["Date"]
            for key, value in data["OrderList"].items():
                OrderList_obj = OrderList()
                OrderList_obj.Customer = customer
                OrderList_obj.Colour = Colour.objects.get(Colour=value["Colour"])
                OrderList_obj.Quality = Quality.objects.get(Quality=value["Quality"])
                OrderList_obj.Order = order
                OrderList_obj.OrderedQuantity = value["Quantity"]
                OrderList_obj.BalanceQuantity = value["Quantity"]
                OrderList_obj.Date = Date
                OrderList_obj.save()
            return redirect('order-booking')
        return render(
            request,
            "order_booking.html",
            context={
                **data,
                "Colours": Colours,
                "Qualities": Qualities,
                **context,
            },
        )
    return render(
        request,
        "order_booking.html",
        context={
            **context,
        },
    )


def stock_view(request):
    return render(request, "stock_view.html")


def consumption_record(request):
    return render(request, "consumption_record.html")


def stock_movement(request):
    return render(request, "stock_movement.html")


def production_input(request):
    return render(request, "production_record.html")
