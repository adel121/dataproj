from django.contrib import admin
from django.contrib import admin
from .models import Manager, Supplier, Delivery_Man, Delivery, Purchase, Product, Bill, Location,Customer,Bill

# Register your models here.

class ManagerAdmin(admin.ModelAdmin):
	list_display=('name','id')

class ProductAdmin(admin.ModelAdmin):
	list_display=('id','category')

class SupplierAdmin(admin.ModelAdmin):
	list_display=('name','id')

class CustomerAdmin(admin.ModelAdmin):
	list_display=('name','id')

class DeliveryAdmin(admin.ModelAdmin):
	list_display=('id','customer')

class BillAdmin(admin.ModelAdmin):
	list_display=('id','bill_number')

class Delivery_ManAdmin(admin.ModelAdmin):
	list_display=('id','name')

admin.site.register(Manager,ManagerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Delivery,DeliveryAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Delivery_Man,Delivery_ManAdmin)
