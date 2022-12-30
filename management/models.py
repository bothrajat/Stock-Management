from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(max_length=256)


class Quality(models.Model):
    Quality = models.CharField(max_length=32, primary_key=True)


class Colour(models.Model):
    Colour = models.CharField(max_length=32, primary_key=True)


class Order(models.Model):
    OrderNo = models.CharField(unique=True, max_length=256)


class SerialNo(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    Order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Date = models.DateField()

    class Meta:
        unique_together = (("Customer", "Order"),)


class OrderList(models.Model):
    SerialNo = models.ForeignKey(SerialNo, on_delete=models.CASCADE)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    OrderedQuantity = models.PositiveIntegerField()
    BalanceQuantity = models.PositiveIntegerField()


class Jobworker(models.Model):
    Role = models.CharField(
        max_length=32,
        choices=[
            ("Office", "Office"),
            ("Dyer", "Dyer"),
            ("Finisher", "Finisher"),
            ("Factory", "Factory"),
        ],
    )
    WorkerName = models.CharField(max_length=64)


class DyeingStock(models.Model):
    Dyer = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class FinishingStock(models.Model):
    Finisher = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class OfficeStock(models.Model):
    Office = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class FactoryStock(models.Model):
    Factory = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class OtherConsumption(models.Model):
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveIntegerField()


class Movement(models.Model):
    FromName = models.ForeignKey(
        Jobworker, on_delete=models.DO_NOTHING, related_name="from_name"
    )
    ToName = models.ForeignKey(
        Jobworker, on_delete=models.DO_NOTHING, related_name="to_name"
    )
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.PositiveBigIntegerField()
