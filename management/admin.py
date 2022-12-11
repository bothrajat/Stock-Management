from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Quality)
admin.site.register(Colour)
admin.site.register(Order)
admin.site.register(OrderList)