from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Quality)
admin.site.register(Colour)
admin.site.register(Jobworker)
admin.site.register(FactoryStock)
admin.site.register(OfficeStock)
admin.site.register(DyeingStock)
admin.site.register(FinishingStock)
admin.site.register(OtherConsumption)
admin.site.register(Movement)
admin.site.register(Challan)