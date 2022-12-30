from django.core.management.base import BaseCommand
import pandas as pd
from management.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('customers.csv')
        for cust in df.Customers:
            model =Customer(CustomerName = cust)
            model.save()

        df1 = pd.read_csv('quality.csv')
        for qual in df1.Quality:
            model =Quality(Quality= qual)
            model.save()

        df2 = pd.read_csv('colour.csv')
        for colo in df2.Colour:
            model = Colour(Colour=colo)
            model.save()

        df3 = pd.read_csv('order.csv')
        for ord in df3.Order:
            model = Order(OrderNo = ord)
            model.save()

        df4 = pd.read_csv('sno.csv')
        for cust, ord, qual, date in zip(df4.Customer, df4.Order, df4.Quality, df4.Date):
            model = SerialNo(Customer=Customer.objects.get(CustomerName = cust), Order = Order.objects.get(OrderNo=ord), Quality=Quality.objects.get(Quality=qual), Date = date)
            model.save()

        