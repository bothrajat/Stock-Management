from django.core.management.base import BaseCommand
import pandas as pd
from management.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # df = pd.read_csv('customers.csv')
        # for cust in df.Customers:
        #     model =Customer(CustomerName = cust)
        #     model.save()

        # df1 = pd.read_csv('quality.csv')
        # for qual in df1.Quality:
        #     model =Quality(Quality= qual)
        #     model.save()

        # df2 = pd.read_csv('colour.csv')
        # for colo in df2.Colour:
        #     model = Colour(Colour=colo)
        #     model.save()

        # df3 = pd.read_csv('order.csv')
        # for ord in df3.Order:
        #     model = Order(OrderNo = ord)
        #     model.save()

        # df4 = pd.read_csv('sno.csv')
        # for cust, ord, qual, date in zip(df4.Customer, df4.Order, df4.Quality, df4.Date):
        #     model = SerialNo(Customer=Customer.objects.get(CustomerName = cust), Order = Order.objects.get(OrderNo=ord), Quality=Quality.objects.get(Quality=qual), Date = date)
        #     model.save()

        # df5  =pd.read_csv('work.csv')
        # for role, name in zip(df5.Role, df5.Name):
        #     model  = Jobworker(Role = role, WorkerName = name)
        #     model.save()

        # df7 = pd.read_csv('finstock.csv')
        # for name, quality, colour, quantity in zip(df7.Finisher, df7.Quality, df7.Colour, df7.Quantity):
        #     model = FinishingStock(Finisher = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(quantity))
        #     model.save()

        # df6 = pd.read_csv('factstock.csv')
        # for name, quality, colour, quantity in zip(df6.Finisher, df6.Quality, df6.Colour, df6.Quantity):
        #     model = FactoryStock(Factory = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(quantity))
        #     model.save()

        # df8 = pd.read_csv('dyestock.csv')
        # for name, quality, colour, quantity in zip(df8.Dyer, df8.Quality, df8.Colour, df8.Quantity):
        #     model = DyeingStock(Dyer = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(quantity))
        #     model.save()

        df9 = pd.read_csv('offstock.csv')
        for name, quality, colour, quantity in zip(df9.Finisher, df9.Quality, df9.Colour, df9.Quantity):
            model = OfficeStock(Office = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(quantity))
            model.save()
