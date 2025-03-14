import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from management.models import *
import json, ast


# Create your views here.
def home(request):
    return redirect("stock-movement")


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


def stock_view(request):
    FactStock = FactoryStock.objects.filter(~Q(Quantity=0))
    OffStock = OfficeStock.objects.filter(~Q(Quantity=0))
    DyeStock = DyeingStock.objects.filter(~Q(Quantity=0))
    FinStock = FinishingStock.objects.filter(~Q(Quantity=0))
    Moves = Movement.objects.all()
    Colours = Colour.objects.all()
    Qualities = Quality.objects.all()
    OtherCons = OtherConsumption.objects.all()

    if request.method == "POST":
        qual = request.POST.get("Quality")
        colour = request.POST.get("Colour")
        print(qual, colour)
        if qual is not None and colour is not None:
            FactStock = FactoryStock.objects.filter(Quality=Quality.objects.get(Quality=qual),
                                                    Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            OffStock = OfficeStock.objects.filter(Quality=Quality.objects.get(Quality=qual),
                                                  Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            DyeStock = DyeingStock.objects.filter(Quality=Quality.objects.get(Quality=qual),
                                                  Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            FinStock = FinishingStock.objects.filter(Quality=Quality.objects.get(Quality=qual),
                                                     Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            Moves = Movement.objects.filter(
                Challan__in=Challan.objects.filter(Quality=Quality.objects.get(Quality=qual)),
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            Colours = Colour.objects.all()
            Qualities = Quality.objects.all()
            OtherCons = OtherConsumption.objects.filter(Quality=Quality.objects.get(Quality=qual),
                                                        Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
        elif qual is not None:
            OffStock = OfficeStock.objects.filter(Quality=Quality.objects.get(Quality=qual)).exclude(Quantity=0)
            DyeStock = DyeingStock.objects.filter(Quality=Quality.objects.get(Quality=qual)).exclude(Quantity=0)
            FinStock = FinishingStock.objects.filter(Quality=Quality.objects.get(Quality=qual)).exclude(Quantity=0)
            Moves = Movement.objects.filter(
                Challan__in=Challan.objects.filter(Quality=Quality.objects.get(Quality=qual))).exclude(Quantity=0)
            Colours = Colour.objects.all()
            Qualities = Quality.objects.all()
            OtherCons = OtherConsumption.objects.filter(Quality=Quality.objects.get(Quality=qual)).exclude(Quantity=0)
        elif colour is not None:
            FactStock = FactoryStock.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            OffStock = OfficeStock.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            DyeStock = DyeingStock.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            FinStock = FinishingStock.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            Moves = Movement.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)
            Colours = Colour.objects.all()
            Qualities = Quality.objects.all()
            OtherCons = OtherConsumption.objects.filter(
                Colour=Colour.objects.get(Colour=colour)).exclude(Quantity=0)

        return render(
            request,
            "stock_view.html",
            context={
                "FactStock": FactStock,
                "OffStock": OffStock,
                "DyeStock": DyeStock,
                "FinStock": FinStock,
                "Moves": Moves,
                "Qualities": Qualities,
                "Colours": Colours,
                "OtherCons": OtherCons
            },
        )

    return render(
        request,
        "stock_view.html",
        context={
            "FactStock": FactStock,
            "OffStock": OffStock,
            "DyeStock": DyeStock,
            "FinStock": FinStock,
            "Moves": Moves,
            "Qualities": Qualities,
            "Colours": Colours,
            "OtherCons": OtherCons
        },
    )


def consumption_record(request):
    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Others = OtherConsumption.objects.all()
    OffStock = OfficeStock.objects.filter(Quantity__gte=1)
    othercons = {}
    for Stock in OffStock:
        othercons[Stock.id] = {
            "Quantity": Stock.Quantity,
            "Colour": Stock.Colour.Colour,
            "Quality": Stock.Quality.Quality
        }
    context = {"Colours": Colours, "Qualities": Qualities, "Othercons": othercons, "Stocks": othercons}
    flag = 0
    if request.method == "POST":
        swit = 1
        otherscons = {}
        for Stock in OfficeStock.objects.filter(Quantity__gte=1):
            othercons[Stock.id] = {
                "Quantity": Stock.Quantity,
                "Colour": Stock.Colour.Colour,
                "Quality": Stock.Quality.Quality
            }

        idee = request.POST.get("ID")
        if idee:
            idee = int(idee)
        else:
            idee = 0
        consumedqty = int(request.POST.get("consumedqty"))
        remark = request.POST.get("remark")
        try:
            with transaction.atomic():
                cons = OfficeStock.objects.get(id=idee)
                cons.Quantity -= consumedqty
                cons.save()

                othercon = OtherConsumption()
                othercon.Colour = cons.Colour
                othercon.Quality = cons.Quality
                othercon.Quantity = consumedqty
                othercon.Remark = remark
                othercon.Date = datetime.date.today()
                othercon.save()

        except Exception as e:
            return HttpResponse(str(e))
            return HttpResponse("Not Possible to Save, Quantity greater than exists", status=500)

        othercons = {}
        for Stock in OfficeStock.objects.filter(Quantity__gte=1):
            othercons[Stock.id] = {
                "Quantity": Stock.Quantity,
                "Colour": Stock.Colour.Colour,
                "Quality": Stock.Quality.Quality
            }
        return render(
            request,
            "consumption_record.html",
            context={
                "Colours": Colours,
                "Qualities": Qualities,
                "Others": Others,
                "Othercons": othercons,
                "Stocks": othercons
            },
        )
    return render(
        request,
        "consumption_record.html",
        context={**context},
    )


def stock_movement(request):
    def data(request):
        data = {}
        data["ChallanNo"] = request.POST.get("challan")
        data["colour"] = request.POST.get("Colour")
        Quantity = request.POST.get("Quantity")
        if Quantity:
            Quantity = int(Quantity)
        else:
            Quantity = 0
        data["Quantity"] = Quantity
        data["Quality"] = request.POST.get("Quality")
        data["fromtype"] = request.POST.get("fromtype")
        data["fromName"] = request.POST.get("fromName")
        data["totype"] = request.POST.get("totype")
        data["toName"] = request.POST.get("toName")
        return data

    def getStockTable(challan):
        if challan.FromName.Role == "Office":
            From = OfficeStock.objects.filter(
                Office=challan.FromName, Quality=challan.Quality
            )
        elif challan.FromName.Role == "Dyer":
            From = DyeingStock.objects.filter(
                Dyer=challan.FromName, Quality=challan.Quality
            )
        elif challan.FromName.Role == "Finisher":
            From = FinishingStock.objects.filter(
                Finisher=challan.FromName, Quality=challan.Quality
            )
        elif challan.FromName.Role == "Factory":
            From = FactoryStock.objects.filter(
                Factory=challan.FromName, Quality=challan.Quality
            )

        if challan.ToName.Role == "Office":
            To = OfficeStock.objects.filter(
                Office=challan.ToName, Quality=challan.Quality
            )
        elif challan.ToName.Role == "Dyer":
            To = DyeingStock.objects.filter(
                Dyer=challan.ToName, Quality=challan.Quality
            )
        elif challan.ToName.Role == "Finisher":
            To = FinishingStock.objects.filter(
                Finisher=challan.ToName, Quality=challan.Quality
            )
        elif challan.ToName.Role == "Factory":
            To = FactoryStock.objects.filter(
                Factory=challan.ToName, Quality=challan.Quality
            )

        return From, To

    Qualities = Quality.objects.all()
    Colours = Colour.objects.all()
    Dyers = Jobworker.objects.filter(Role="Dyer")
    Finishers = Jobworker.objects.filter(Role="Finisher")
    Factories = Jobworker.objects.filter(Role="Factory")
    Offices = Jobworker.objects.filter(Role="Office")
    context = {
        "Colours": Colours,
        "Qualities": Qualities,
        "Dyers": json.dumps([dyer.WorkerName for dyer in Dyers]),
        "Finishers": json.dumps([finisher.WorkerName for finisher in Finishers]),
        "Factories": json.dumps([factory.WorkerName for factory in Factories]),
        "Offices": json.dumps([office.WorkerName for office in Offices]),
    }
    if request.method == "POST":
        if request.POST.get("STOCK"):
            data = data(request)
            StockList = request.POST.get("StockList")
            ID = request.POST.get("ID")
            if StockList and StockList != "{}":
                StockList = ast.literal_eval(StockList)
                if not ID:
                    ID = max(StockList.keys()) + 1
                else:
                    ID = int(ID)
            else:
                StockList = {}
                ID = 1
            if data['Quantity'] > 0:
                StockList[ID] = {
                    "Colour": data["colour"],
                    "Quantity": data["Quantity"],
                }
            BalanceStock = {}
            if data['fromtype'] == "Dyeing":
                for i, stock in enumerate(
                        DyeingStock.objects.filter(Dyer=Jobworker.objects.get(WorkerName=data['fromName']),
                                                   Quality=Quality.objects.get(Quality=data['Quality']),
                                                   Colour=Colour.objects.get(Colour=data['colour']))):
                    BalanceStock[i] = {
                        "Quantity": stock.Quantity,
                        "Quality": stock.Quality,
                        "Colour": stock.Colour
                    }
            elif data['fromtype'] == "Finishing":
                for i, stock in enumerate(
                        FinishingStock.objects.filter(Finisher=Jobworker.objects.get(WorkerName=data['fromName']),
                                                      Quality=Quality.objects.get(Quality=data['Quality']),
                                                      Colour=Colour.objects.get(Colour=data['colour']))):
                    BalanceStock[i] = {
                        "Quantity": stock.Quantity,
                        "Quality": stock.Quality,
                        "Colour": stock.Colour
                    }
            return render(
                request,
                "stock_movement.html",
                context={
                    **context,
                    **data,
                    "BalanceStock": BalanceStock,
                    "StockList": StockList,
                },
            )

        if request.POST.get("SEARCH"):
            challan = Challan.objects.get(ChallanNo=int(request.POST.get("challan")))
            StockList, data = {}, {}
            data["Quality"] = challan.Quality.Quality
            data["fromtype"] = challan.FromName.Role
            data["fromName"] = challan.FromName.WorkerName
            data["totype"] = challan.ToName.Role
            data["toName"] = challan.ToName.WorkerName
            data["ChallanNo"] = challan.ChallanNo
            for idx, movement in enumerate(Movement.objects.filter(Challan=challan)):
                StockList[idx + 1] = {
                    "Colour": movement.Colour.Colour,
                    "Quantity": movement.Quantity,
                }

            return render(
                request,
                "stock_movement.html",
                context={
                    **context,
                    **data,
                    "StockList": StockList,
                },
            )

        if request.POST.get("SAVE"):
            data = data(request)
            StockList = request.POST.get("StockList")
            ID = request.POST.get("ID")
            if StockList and StockList != "{}":
                StockList = ast.literal_eval(StockList)
                if not ID:
                    ID = max(StockList.keys()) + 1
                else:
                    ID = int(ID)
            else:
                StockList = {}
                ID = 1
            StockList[ID] = {
                "Colour": data["colour"],
                "Quantity": data["Quantity"],
            }

            return render(
                request,
                "stock_movement.html",
                context={
                    **context,
                    **data,
                    "StockList": StockList,
                },
            )

        if request.POST.get("REMOVE"):
            data = data(request)
            StockList = ast.literal_eval(request.POST.get("StockList"))
            ID = int(request.POST.get("ID"))
            del StockList[ID]
            if not StockList:
                return redirect("stock-movement")

            return render(
                request,
                "stock_movement.html",
                context={
                    **context,
                    **data,
                    "StockList": StockList,
                },
            )

        if request.POST.get("Submit"):
            data = data(request)
            StockList = ast.literal_eval(request.POST.get("StockList"))
            try:
                challan = Challan.objects.get(ChallanNo=data["ChallanNo"])
                From, To = getStockTable(challan)
                MovementList = Movement.objects.filter(Challan=challan)
                try:
                    with transaction.atomic():
                        for movement in MovementList:
                            if challan.FromName.Role != 'Factory':
                                changeFrom = From.get(Colour=movement.Colour)
                                changeFrom.Quantity -= movement.Quantity
                            changeTo = To.get(Colour=movement.Colour)
                            changeTo.Quantity += movement.Quantity
                            changeTo.save()
                            if challan.FromName.Role != 'Factory':
                                changeFrom.save()
                        MovementList.delete()
                except Exception as e:
                    return HttpResponse(str(e))
            except:
                challan = Challan()
                challan.ChallanNo = data["ChallanNo"]
                challan.FromName = Jobworker.objects.get(WorkerName=data["fromName"])
                challan.ToName = Jobworker.objects.get(WorkerName=data["toName"])
                challan.Quality = Quality.objects.get(Quality=data["Quality"])
                challan.save()
            From, To = getStockTable(challan)
            try:
                with transaction.atomic():
                    for key, value in StockList.items():
                        movement = Movement()
                        movement.Challan = challan
                        movement.Colour = Colour.objects.get(Colour=value["Colour"])
                        movement.Quantity = value["Quantity"]
                        movement.Date = datetime.date.today()
                        if challan.FromName.Role != 'Factory':
                            changeFrom = From.get(Colour=movement.Colour)
                            changeFrom.Quantity -= movement.Quantity
                        changeTo = To.get(Colour=movement.Colour)
                        changeTo.Quantity += movement.Quantity
                        changeTo.save()
                        if challan.FromName.Role != 'Factory':
                            changeFrom.save()
                        movement.save()
            except Exception as e:
                return HttpResponse(str(e))

    return render(
        request,
        "stock_movement.html",
        context={
            **context,
        },
    )
