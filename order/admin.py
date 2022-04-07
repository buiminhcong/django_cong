from django.contrib import admin
from .models import Cart, Cash, Credit, Transfer, Order, CartBookItem, Shipment, OrderBookItem
# Register your models here.

admin.site.register(Cart)
admin.site.register(Cash)
admin.site.register(Credit)
admin.site.register(Transfer)
admin.site.register(Order)
admin.site.register(CartBookItem)
admin.site.register(OrderBookItem)
admin.site.register(Shipment)