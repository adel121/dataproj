from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
urlpatterns = [
   path('',views.index,name="index"),
   path('suppliers/',views.suppliers,name="suppliers"),
   path('supplier/<int:id>/',views.supplier,name="supplier"),
   path('managers/',views.managers,name="managers"),
   path('drivers/',views.drivers,name="drivers"),
   path('driver/<int:id>/',views.driver,name="driver"),
   path('locations/',views.locations,name="locations"),
   path('location/<int:id>',views.location,name="location"),
   path('customers/',views.customers,name="customers"),
   path('customer/<int:id>/',views.customer,name="customer"),
   path('products/',views.products,name="products"),
   path('product/<int:id>/',views.product,name="product"),
   path('deliveries/',views.deliveries,name="deliveries"),
   path('delivery/<int:id>/',views.delivery,name="delivery"),
   path('manager/<int:id>/',views.manager,name="manager"),
   path('bills/',views.bills,name="bills"),
   path('bill/<int:id>/',views.bill,name="bill"),
   path('purchases/',views.purchases,name="purchases"),
   path('purchase/<int:id>',views.purchase,name="purchase")
]
