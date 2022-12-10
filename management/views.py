from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from management.models import *

# Create your views here.


def home(request):
    return redirect("order-booking")


def order_booking(request):
    return render(request, "order-booking.html")


def stock_view(request):
    return render(request, "stock-view.html")


def consumption_record(request):
    return render(request, "consumption-record.html")


def stock_movement(request):
    return render(request, "stock-movement.html")


def production_input(request):
    return render(request, "production-input.html")
