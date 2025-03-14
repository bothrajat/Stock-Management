from django.db import models

# Create your models here.


class Quality(models.Model):
    Quality = models.CharField(max_length=32, primary_key=True)


class Colour(models.Model):
    Colour = models.CharField(max_length=32, primary_key=True)



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
    Quantity = models.IntegerField()


class FinishingStock(models.Model):
    Finisher = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.IntegerField()


class OfficeStock(models.Model):
    Office = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.IntegerField()


class FactoryStock(models.Model):
    Factory = models.ForeignKey(Jobworker, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.IntegerField()


class OtherConsumption(models.Model):
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.IntegerField()
    Remark = models.TextField(null=True)
    Date = models.DateField()


class Challan(models.Model):
    ChallanNo = models.PositiveIntegerField(primary_key=True)
    FromName = models.ForeignKey(
        Jobworker, on_delete=models.DO_NOTHING, related_name="from_name"
    )
    ToName = models.ForeignKey(
        Jobworker, on_delete=models.DO_NOTHING, related_name="to_name"
    )
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)


class Movement(models.Model):
    Challan = models.ForeignKey(Challan, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quantity = models.BigIntegerField()
    Date = models.DateField()
