from django.db import models

# Create your models here.

class Manager(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	name=models.CharField(default='none',max_length=30,unique=True)
	tel_num=models.CharField(default=0,max_length= 20)
	is_deleted=models.BooleanField(default=False)

class Supplier(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	name=models.CharField(default='none',max_length=30,unique=True,)
	tel_num=models.CharField(default=0,max_length= 20)
	is_deleted=models.BooleanField(default=False)

class Delivery_Man(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	name=models.CharField(default='none',max_length=30,unique=True)
	tel_num=models.CharField(default=0,max_length= 20)
	is_deleted=models.BooleanField(default=False)



class Location(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	country=models.CharField(default='none',max_length=30)
	city=models.CharField(default='none',max_length=30)
	street=models.CharField(default='none',max_length=30)
	building=models.CharField(default='none',max_length=30)
	floor=models.IntegerField(default=0)
	is_deleted=models.BooleanField(default=False)

class Product(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	category=models.CharField(default='none',max_length=30,unique=True)
	unit_price=models.PositiveIntegerField(default='none')
	unit_mass=models.PositiveIntegerField(default='none')
	is_deleted=models.BooleanField(default=False)


class Customer(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	name=models.CharField(default='none',max_length=30,unique=True)
	tel_num=models.CharField(default=0,max_length= 20)
	is_deleted=models.BooleanField(default=False)

class Delivery(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	driver_in=models.ForeignKey(Delivery_Man,on_delete=models.DO_NOTHING,related_name='driver_in')
	driver_out=models.ForeignKey(Delivery_Man,on_delete=models.DO_NOTHING, related_name='driver_out')
	location_from=models.ForeignKey(Location,on_delete=models.DO_NOTHING,related_name='location_from')
	location_to=models.ForeignKey(Location,on_delete=models.DO_NOTHING,related_name='location_to')
	customer=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)



Status_Choices = ( ('paid','PAID'), ('pending','PENDING'), ('sent','SENT'), ('refunded','REFUNDED'), ('finalized','FINALIZED'))

class Bill(models.Model):
	bill_number=models.IntegerField(null=False,unique=True)
	id=models.IntegerField(null=False,primary_key=True)
	delivery_charge=models.PositiveIntegerField(default=0)
	date=models.DateField(default='none',max_length=30)
	delivery=models.ForeignKey(Delivery,on_delete=models.DO_NOTHING)
	manager=models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
	status=models.CharField(max_length=99, choices=Status_Choices, default="pending" )
	is_deleted=models.BooleanField(default=False)

class Purchase(models.Model):
	id=models.IntegerField(null=False,primary_key=True)
	quantity=models.IntegerField(default=0)
	supplier=models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
	product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
	bill=models.ForeignKey(Bill,on_delete=models.DO_NOTHING)