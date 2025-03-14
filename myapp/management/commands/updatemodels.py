from django.core.management.base import BaseCommand
import pandas as pd
from management.models import *




class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        df1 = pd.read_csv('quality.csv')
        # for qual in df1.Quality:
        #     model =Quality(Quality= qual)
        #     model.save()

        df2 = pd.read_csv('colour.csv')
        # for colo in df2.Colour:
        #     model = Colour(Colour=colo)
        #     model.save()

        df5 = pd.read_csv('work.csv')
        # for role, name in zip(df5.Role, df5.Name):
        #     model  = Jobworker(Role = role, WorkerName = name)
        #     model.save()

        # df7 = pd.read_csv('finstock.csv')
        # for name in df7.Finisher:
        #     for quality in df1.Quality:
        #         for colour in df2.Colour:
        #             try:
        #                 model = FinishingStock(Finisher = Jobworker.objects.get(Role="Finisher", WorkerName=name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(0))
        #                 model.save()
        #             except Exception as e:
        #                 print(name)
        #
        df6 = pd.read_csv('factstock.csv')
        for name in df6.Factory:
            for quality in df1.Quality:
                for colour in df2.Colour:
                    try:
                        model = FactoryStock(Factory = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(0))
                        model.save()
                    except Exception as e:
                        print(name)
        #
        df8 = pd.read_csv('dyestock.csv')
        for name in df8.Dyer:
            for quality in df1.Quality:
                for colour in df2.Colour:
                    try:
                        model = DyeingStock(Dyer = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(0))
                        model.save()
                    except Exception as e:
                        print(name)
        #
        df9 = pd.read_csv('offstock.csv')
        for name in df9.Office:
            for quality in df1.Quality:
                for colour in df2.Colour:
                    try:
                        model = OfficeStock(Office = Jobworker.objects.get(WorkerName = name), Quality = Quality.objects.get(Quality = quality), Colour = Colour.objects.get(Colour = colour), Quantity = int(0))
                        model.save()
                    except Exception as e:
                        print(name)
