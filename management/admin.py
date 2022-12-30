from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Quality)
admin.site.register(Colour)
admin.site.register(Order)
admin.site.register(Jobworker)
admin.site.register(FactoryStock)
admin.site.register(OfficeStock)
admin.site.register(DyeingStock)
admin.site.register(FinishingStock)
admin.site.register(OrderList)
admin.site.register(SerialNo)
admin.site.register(OtherConsumption)
admin.site.register(Movement)