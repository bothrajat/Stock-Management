from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(max_length=256)


class Quality(models.Model):
    Quality = models.CharField(max_length=32, primary_key=True)


class Colour(models.Model):
    Colour = models.CharField(max_length=32, primary_key=True)


class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    Colour = models.ForeignKey(Colour, on_delete=models.DO_NOTHING)
    Quality = models.ForeignKey(Quality, on_delete=models.DO_NOTHING)
    OrderNo = models.PositiveBigIntegerField()
    OrderedQuantity = models.PositiveIntegerField()
    BalanceQuantity = models.PositiveIntegerField()
    Date = models.DateField()


# Dying
# Finishing

"""create table quality(qual varchar(256) primary key);
create table colour(col varchar(256) primary key);
drop table customerName;
create table customerName(name varchar(256) primary key,
 city varchar(256));
select * from orderdata;
create table orderdata(
srno int(10) primary key auto_increment,
orderno int(10),
dateorder date,
custname varchar(256),
quality varchar(256),
colour varchar(256),
initial_quantity int(10),
balance_quantity int(10),
foreign key(colour) references colour(col),
foreign key(quality) references quality(qual),
foreign key(custname) references customerName(name)
 );"""
