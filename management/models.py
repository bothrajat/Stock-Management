from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(max_length=256)


class Quality(models.Model):
    Quality = models.CharField(max_length=32, primary_key=True)


class Colour(models.Model):
    Colour = models.CharField(max_length=32, primary_key=True)

class Order(models.Model):
    OrderNo=models.IntegerField(unique=True)

class OrderList(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    OrderedQuantity = models.PositiveIntegerField()
    BalanceQuantity = models.PositiveIntegerField()
    Date = models.DateField()

class Office(models.Model):
    Name=models.CharField(max_length=10, unique=True)

class Factory(models.Model):
    Name=models.CharField(max_length=20, unique=True)

class Dyer(models.Model):
    Name=models.CharField(max_length=256, unique=True)

class Finisher(models.Model):
    Name = models.CharField(max_length=256, unique=True)

# class Stock(models.Model):
#     Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
#     Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
#     Quantity = models.PositiveIntegerField()
#     Type = models.ForeignKey(Typeofplace, on_delete=models.DO_NOTHING)
#     Name = models.CharField(max_length=256)

class DyeingStock(models.Model):
    Dyer = models.ForeignKey(Dyer, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()

class FinishingStock(models.Model):
    Finisher = models.ForeignKey(Finisher, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()

class OfficeStock(models.Model):
    Office=models.ForeignKey(Office,on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()

class FactoryStock(models.Model):
    Factory=models.ForeignKey(Factory,on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()

class OtherConsumption(models.Model):
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()