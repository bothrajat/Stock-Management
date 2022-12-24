from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.db import transaction
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
        "OrderNo": request.POST.get("OrderNo"),
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
    serialNo = SerialNo.objects.count() + 1
    Orderlist = {}
    context = {
        "SerialNo": serialNo,
        "Colours": Colours,
        "Qualities": Qualities,
        "Customers": Customers,
    }
    if request.method == "POST":
        data = collect(request)

        if request.POST.get("save"):
            data["OrderList"][data["ID"]] = {
                "Colour": data["Colour"],
                "Quantity": data["Quantity"],
            }

        elif request.POST.get("remove"):
            del data["OrderList"][data["ID"]]
            if not data["OrderList"]:
                return redirect("order-booking")

        elif request.POST.get("submit"):
            try:
                with transaction.atomic():
                    try:
                        order = Order.objects.get(OrderNo=data["OrderNo"])
                    except:
                        order = Order.objects.create(OrderNo=data["OrderNo"])
                    # print(data["CustomerName"])
                    customer = Customer.objects.get(CustomerName=data["CustomerName"])
                    quality = Quality.objects.get(Quality=data["Quality"])
                    serialNo = SerialNo.objects.create(Order=order, Customer=customer,Quality=quality)
                    Date = data["Date"]
                    for key, value in data["OrderList"].items():
                        OrderList_obj = OrderList()
                        OrderList_obj.SerialNo=serialNo
                        OrderList_obj.Colour = Colour.objects.get(Colour=value["Colour"])
                        OrderList_obj.OrderedQuantity = value["Quantity"]
                        OrderList_obj.BalanceQuantity = value["Quantity"]
                        OrderList_obj.Date = Date
                        OrderList_obj.save()
                    return redirect("order-booking")
            except:
                print("Error OCCURREDD")

        return render(
            request,
            "order_booking.html",
            context={
                **data,
                **context,
            },
        )
    return render(
        request,
        "order_booking.html",
        context={
            **context,
            "OrderList": Orderlist,
        },
    )


def stock_view(request):
    FactStock = FactoryStock.objects.all()
    OffStock = OfficeStock.objects.all()
    DyeStock = DyeingStock.objects.all()
    Orders = OrderList.objects.all().order_by("Order")
    FinStock = FinishingStock.objects.all()

    return render(
        request,
        "stock_view.html",
        context={
            "FactStock": FactStock,
            "OffStock": OffStock,
            "DyeStock": DyeStock,
            "Orders": Orders,
            "FinStock": FinStock,
        },
    )


def consumption_record(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Customers = Customer.objects.all()
    Orders = OrderList.objects.all()
    Others = OtherConsumption.objects.all()
    context = {"Customers": Customers, "Colours": Colours, "Qualities": Qualities}
    flag = 0
    if request.method == "POST":
        if request.POST.get("search"):
            flag = 1
            quality = request.POST.get("quality")
            colour = request.POST.get("colour")
            swit = int(request.POST.get("swit"))
            customer = request.POST.get("customer")
            otherscons = {}
            stocks = {}
            print(swit)
            if swit:
                try:
                    print("I am in try")
                    for number in OtherConsumption.objects.all():
                        otherscons[number.id] = {
                            "Quality":number.Quality.Quality,
                            "Colour":number.Colour.Colour,
                            "Quantity":number.Quantity
                        }
                except:
                    otherscons = None
            else:
                try:
                    
                    for number in SerialNo.objects.filter(Customer = Customer.objects.get(CustomerName = customer)):
                        for order in OrderList.objects.filter(SerialNo = number):
                            stocks[order.id] = {
                                "OrderNo": order.SerialNo.Order.OrderNo,
                                "CustomerName":order.SerialNo.Customer.CustomerName,
                                "Quality": order.SerialNo.Quality.Quality,
                                "Colour": order.Colour.Colour,
                                "OrderedQuantity" : order.OrderedQuantity,
                                "BalanceQuantity":order.BalanceQuantity,
                                "Date": str(order.Date)
                            }
                except:
                    stocks = None
           
            return render(
                    request,
                    "consumption_record.html",
                    context={
                        "Orders": Orders,
                        "Colours": Colours,
                        "Qualities": Qualities,
                        "Customers": Customers,
                        "Others": Others,
                        "Stocks": stocks,
                        "Othercons":otherscons
                    },
                )
        
        if request.POST.get("submit"):
           
            idee = (request.POST.get("ID"))
            if idee:
                idee = int(idee)
            else:
                idee = 0
            consumedqty = int(request.POST.get("consumedqty"))
            otherscons = {}
            swit = int(request.POST.get("swit"))
            stocks = {}
            if not swit:
                customer = request.POST.get("customer")
                
                ordertook = OrderList.objects.get(id = idee)
                ordertook.BalanceQuantity -= consumedqty
                ordertook.save()
                for number in SerialNo.objects.filter(Customer = Customer.objects.get(CustomerName = customer)):
                    for order in OrderList.objects.filter(SerialNo = number):
                        stocks[order.id] = {
                                "OrderNo": order.SerialNo.Order.OrderNo,
                                "CustomerName":order.SerialNo.Customer.CustomerName,
                                "Quality": order.SerialNo.Quality.Quality,
                                "Colour": order.Colour.Colour,
                                "OrderedQuantity" : order.OrderedQuantity,
                                "BalanceQuantity":order.BalanceQuantity,
                                "Date": str(order.Date)
                            }

            else:
                
                if idee <= 0:
                    quality = request.POST.get("Quality")
                    colour =request.POST.get("Colour")
                    cons = OtherConsumption()
                    cons.Quality = Quality.objects.get(Quality = quality)
                    cons.Colour = Colour.objects.get(Colour = colour)
                    cons.Quantity = consumedqty
                    cons.save()
                else:
                    cons = OtherConsumption.objects.get(id = idee)
                    cons.Quantity += consumedqty
                    cons.save()

                for number in OtherConsumption.objects.all():
                    otherscons[number.id] = {
                            "Quality":number.Quality.Quality,
                            "Colour":number.Colour.Colour,
                            "Quantity":number.Quantity
                        }
            return render(
                    request,
                    "consumption_record.html",
                    context={
                        "Orders": Orders,
                        "Colours": Colours,
                        "Qualities": Qualities,
                        "Customers": Customers,
                        "Others": Others,
                        "Stocks": stocks,
                        "Othercons":otherscons
                    },
                )

            



            
    return render(
        request,
        "consumption_record.html",
        context={**context},
    )


def stock_movement(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Dyers = Dyer.objects.all()
    Finishers = Finisher.objects.all()
    Offices = Office.objects.all()
    Factories = Factory.objects.all()
    context = {
        "Colours": Colours,
        "Qualities": Qualities,
        "Dyers": json.dumps([dyer.Name for dyer in Dyers]),
        "Finishers": json.dumps([finisher.Name for finisher in Finishers]),
        "Factories": json.dumps([factory.Name for factory in Factories]),
        "Offices": json.dumps([office.Name for office in Offices]),
    }
    if request.method == "POST":
        data = {}
        data["StockList"] = request.POST.get("stocklist")
        data["ID"] = request.POST.get("ID")
        data["quality"] = request.POST.get("Quality")
        data["colour"] = request.POST.get("Colour")
        data["Quantity"] = int(request.POST.get("Quantity", 0))
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

            return render(
                    request,
                    "consumption_record.html",
                    context={
                        **context,
                        "StockList": StockList
                    }
                )

    return render(request, "stock_movement.html", context=context)


def production_input(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Factories = Factory.objects.all()
    context = {
        "Colours": Colours,
        "Qualities": Qualities,
        "Factories": Factories,
    }
    if request.method == "POST":
        quality = request.POST.get("Quality")
        colour = request.POST.get("Colour")
        factory = Factory.objects.get(Name=request.POST.get("Factory"))
        Quantity = int(request.POST.get("Quantity", 0))
        try:
            stocks = FactoryStock.objects.get(
                Factory=factory,
                Quality=Quality.objects.get(Quality=quality),
                Colour=Colour.objects.get(Colour=colour),
            )
            stocks.Quantity += Quantity
            stocks.save()

        except:
            stock = FactoryStock()
            stock.Factory = factory
            stock.Quality = Quality.objects.get(Quality=quality)
            stock.Colour = Colour.objects.get(Colour=colour)
            stock.Quantity = Quantity
            stock.save()

    return render(
        request,
        "production_record.html",
        context={**context},
    )
