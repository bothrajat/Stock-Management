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
    FactStock = FactoryStock.objects.all()
    OffStock = OfficeStock.objects.all()
    DyeStock = DyeingStock.objects.all()
    Orders = OrderList.objects.all()
    FinStock = FinishingStock.objects.all()


    return render(request, "stock_view.html", context={"FactStock":FactStock, "OffStock":OffStock, "DyeStock":DyeStock, "Orders":Orders, "FinStock":FinStock})


def consumption_record(request):
    return render(request, "consumption_record.html")


def stock_movement(request):
     
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Dyers = Dyer.objects.all()
    Finishers = Finisher.objects.all()
    if request.method=="POST":
        data={}
        data["StockList"] = request.POST.get("stocklist")
        data["ID"] = request.POST.get("ID")
        data["quality"]=request.POST.get("Quality")
        data["colour"]= request.POST.get("Colour")
        data["Quantity"]= int(request.POST.get("Quantity", 0))
        data["FromType"] = request.POST.get("fromtype")
        data["FromName"] = request.POST.get("fromName")
        data["ToType"] = request.POST.get("totype")
        data["ToName"] = request.POST.get("toName")
        if not StockList:
            StockList = {}
            ID = 1
        else:
            StockList = ast.literal_eval(StockList)
            if not ID:
                ID = max(StockList.keys()) + 1
            else:
                ID = int(ID)

        if request.POST.get("save"):
            data["StockList"][data["ID"]] = {
                "Quality": data["Quality"],
                "Colour": data["Colour"],
                "Quantity": data["Quantity"],
            }

    return render(request, "stock_movement.html")


def production_input(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    if request.method =="POST":
        quality=request.POST.get("Quality")
        colour= request.POST.get("Colour")
        Quantity= int(request.POST.get("Quantity", 0))
        try:
            stocks=FactoryStock.objects.get(Quality=Quality.objects.get(Quality=quality), Colour=Colour.objects.get(Colour=colour)) 
            stocks.Quantity+=Quantity
            stocks.save()

        except :
           stock = FactoryStock()
           stock.Quality = Quality.objects.get(Quality=quality)
           stock.Colour=Colour.objects.get(Colour=colour)
           stock.Quantity=Quantity
           stock.save()
         
    return render (request, "production_record.html", context={"Colours": Colours,
            "Qualities": Qualities})
