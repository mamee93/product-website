from django.contrib import admin
from .models import Customer,Order,Product,OrderItem,ShippingAddres
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddres)