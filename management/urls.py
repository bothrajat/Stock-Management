from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order-booking/', views.order_booking, name='order-booking'),
    path('stock-view/', views.stock_view, name='stock-view'),
    path('consumption-record/', views.consumption_record, name='consumption-record'),
    path('stock-movement/', views.stock_movement, name='stock-movement'),
    path('production-input/', views.production_input, name='production-input'),
    path('edit-order/', views.edit_order, name='edit-order'),
]
