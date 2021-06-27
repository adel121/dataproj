from django.shortcuts import render,HttpResponse
from .models import Manager, Supplier, Delivery_Man, Delivery, Purchase, Product, Bill, Location,Customer
from . import queries as q
# Create your views here.
def index(request):
	return render(request, 'index.html')

def suppliers(request):
	queries = []
	if request.method == "POST":
		name = request.POST.get('name')
		tel_num = request.POST.get('tel_num')
		q.execute_query(q.INSERT.format("supplier") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
		queries.append(q.INSERT.format("supplier") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
	suppliers= list(q.execute_query("select id,name, tel_num from deliveryapp_supplier where is_deleted <> 1 "))
	queries.append("select id,name, tel_num from deliveryapp_supplier where is_deleted <> 1 ")
	return render(request,'suppliers.html',{'suppliers':suppliers, 'queries':queries})

def customers(request):
	queries = []
	if request.method == "POST":
		name = request.POST.get('name')
		tel_num = request.POST.get('tel_num')
		q.execute_query(q.INSERT.format("customer") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
		queries.append(q.INSERT.format("customer") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
	customers= list(q.execute_query("select id,name, tel_num from deliveryapp_customer where is_deleted <> 1 "))
	queries.append("select id,name, tel_num from deliveryapp_customer where is_deleted <> 1 ")
	return render(request,'customers.html',{'customers':customers, 'queries':queries})


def products(request):
	queries = []
	if request.method == "POST":
		category = request.POST.get('category')
		unit_price = request.POST.get('unit_price')
		unit_mass= request.POST.get('unit_mass')
		q.execute_query(q.INSERT.format("product") + q.INSERT_AUX(["category","unit_price","unit_mass","is_deleted"],["'"+category+"'",str(unit_price),str(unit_mass),"0"]))
		queries.append(q.INSERT.format("product") + q.INSERT_AUX(["category","unit_price","unit_mass","is_deleted"],["'"+category+"'",str(unit_price),str(unit_mass),"0"]))
	products= list(q.execute_query("select id,category, unit_price,unit_mass from deliveryapp_product where is_deleted <> 1 "))
	print(products)
	queries.append("select id,category, unit_price,unit_mass from deliveryapp_product where is_deleted <> 1 ")
	return render(request,'products.html',{'products':products, 'queries':queries})


def managers(request):
	queries = []
	if request.method == "POST":
		name = request.POST.get('name')
		tel_num = request.POST.get('tel_num')
		q.execute_query(q.INSERT.format("manager") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
		queries.append(q.INSERT.format("manager") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
	managers= list(q.execute_query("select id,name, tel_num from deliveryapp_manager where is_deleted <> 1 "))
	queries.append("select id,name, tel_num from deliveryapp_manager where is_deleted <> 1 ")
	return render(request,'managers.html',{'managers':managers, 'queries':queries})

def drivers(request):
	queries = []
	if request.method == "POST":
		name = request.POST.get('name')
		tel_num = request.POST.get('tel_num')
		q.execute_query(q.INSERT.format("delivery_man") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
		queries.append(q.INSERT.format("delivery_man") + q.INSERT_AUX(["name","tel_num","is_deleted"],["'"+name+"'","'"+tel_num+"'","0"]))
	drivers= list(q.execute_query("select id,name, tel_num from deliveryapp_delivery_man where is_deleted <> 1 "))
	queries.append("select id,name, tel_num from deliveryapp_delivery_man where is_deleted <> 1 ")
	return render(request,'drivers.html',{'drivers':drivers, 'queries':queries})


def locations(request):
	queries = []
	if request.method == "POST":
		country = request.POST.get('country')
		city= request.POST.get('city')
		street = request.POST.get('street')
		building = request.POST.get('building')
		floor = request.POST.get('floor')
		q.execute_query(q.INSERT.format("location") + q.INSERT_AUX(["country","city","street","building","floor","is_deleted"],["'"+country+"'","'"+city+"'","'"+street+"'","'"+building+"'",str(floor),"0"]))
		queries.append(q.INSERT.format("location") + q.INSERT_AUX(["country","city","street","building","floor","is_deleted"],["'"+country+"'","'"+city+"'","'"+street+"'","'"+building+"'",str(floor),"0"]))
	locations= list(q.execute_query("select id,country, city, street,building,floor from deliveryapp_location where is_deleted <> 1 "))
	queries.append("select id,country, city, street,building,floor from deliveryapp_location where is_deleted <> 1 ")
	return render(request,'locations.html',{'locations':locations, 'queries':queries})




def location(request,id):
	queries = [] 
	location = list(q.execute_query("select id, country, city, street,building, floor from deliveryapp_location where id = {0}".format(str(id))))[0]
	queries.append("select id, country, city, street,building, floor from deliveryapp_location where id = {0}".format(str(id)))
	return render(request, "location.html", {'location':location, 'queries':queries})

def product(request,id):
	queries = []  
	product = list(q.execute_query("select id, category, unit_price, unit_mass from deliveryapp_product where id = {0}".format(str(id))))[0]
	queries.append("select id, category, unit_price, unit_mass from deliveryapp_product where id = {0}".format(str(id)))
	return render(request, "product.html",{'product':product, 'queries':queries})

def manager(request,id):
	queries = [] 
	manager = list(q.execute_query("select id,name, tel_num from deliveryapp_manager where id = {0}".format(str(id))))[0]
	queries.append("select id,name, tel_num from deliveryapp_manager where id = {0}".format(str(id)))
	return render(request,'manager.html',{'queries':queries, 'manager':manager})


def supplier(request,id):
	queries = [] 
	supplier = list(q.execute_query("select id,name, tel_num from deliveryapp_supplier where id = {0}".format(str(id))))[0]
	queries.append("select id,name, tel_num from deliveryapp_supplier where id = {0}".format(str(id)))
	return render(request,'supplier.html',{'queries':queries, 'supplier':supplier})

def customer(request,id):
	queries = [] 
	customer = list(q.execute_query("select id,name, tel_num from deliveryapp_customer where id = {0}".format(str(id))))[0]
	queries.append("select id,name, tel_num from deliveryapp_customer where id = {0}".format(str(id)))
	return render(request,'customer.html',{'queries':queries, 'customer':customer})

def driver(request,id):
	queries = [] 
	driver = list(q.execute_query("select id,name, tel_num from deliveryapp_delivery_man where id = {0}".format(str(id))))[0]
	queries.append("select id,name, tel_num from deliveryapp_delivery_man where id = {0}".format(str(id)))
	return render(request,'driver.html',{'queries':queries, 'driver':driver})





def deliveries(request):
	queries = []
	if request.method == "POST":
		driver_in = request.POST.get('driver_in')
		driver_out = request.POST.get('driver_out')
		location_from = request.POST.get('location_from')
		location_to = request.POST.get('location_to')
		customer = request.POST.get('customer')
		query_add = q.INSERT.format("delivery") + q.INSERT_AUX(["driver_in_id","driver_out_id","location_from_id","location_to_id","customer_id"],[str(driver_in),str(driver_out),str(location_from),str(location_to),str(customer)])
		q.execute_query(query_add)
		queries.append(query_add)
	query_driver_man = "select id, name from deliveryapp_delivery_man where is_deleted <> 1"
	query_location = "select id, country, city, street, building ,floor from deliveryapp_location where is_deleted <> 1"
	query_customer ="select id, name from deliveryapp_customer where is_deleted <> 1"
	customers=list(q.execute_query(query_customer))
	driver_men = list(q.execute_query(query_driver_man))
	locations = list(q.execute_query(query_location))
	queries.append(query_driver_man)
	queries.append(query_location)
	queries.append(query_customer)
	deliveries = q.execute_query("select id from deliveryapp_delivery")
	queries.append("select id from deliveryapp_delivery")
	return render(request, "deliveries.html",{'deliveries':deliveries,'customers':customers,'locations':locations,'driver_men':driver_men,'queries':queries})



def bills(request):
	queries = []
	if request.method == "POST":
		bill_number = request.POST.get('bill_number')
		delivery_charge = request.POST.get('delivery_charge')
		manager = request.POST.get('manager')
		delivery = request.POST.get('delivery')
		date = request.POST.get('date')
		query_add = q.INSERT.format("bill") + q.INSERT_AUX(["bill_number","delivery_charge","manager_id","delivery_id","date","status","is_deleted"],[str(bill_number),str(delivery_charge),str(manager),str(delivery),"'"+date+"'","'pending'","0"])
		q.execute_query(query_add)
		queries.append(query_add)
	query_manager = "select id, name from deliveryapp_manager where is_deleted <> 1"
	query_delivery = "select id from deliveryapp_delivery"
	queries.append(query_manager)
	queries.append(query_delivery)
	managers=list(q.execute_query(query_manager))
	deliveries=list(q.execute_query(query_delivery)) 
	bills = list(q.execute_query("select id, bill_number from deliveryapp_bill where is_deleted <> 1"))
	queries.append("select id, bill_number from deliveryapp_bill where is_deleted <> 1")
	return render(request,"bills.html",{'bills':bills, 'queries':queries, 'managers':managers, 'deliveries':deliveries})



def purchases(request):
	queries = []
	if request.method == "POST":
		quantity = request.POST.get('quantity')
		supplier = request.POST.get('supplier')
		product = request.POST.get('product')
		bill = request.POST.get('bill')
		query_add = q.INSERT.format("purchase") + q.INSERT_AUX(["quantity","supplier_id","product_id","bill_id"],[str(quantity),str(supplier),str(product),str(bill)])
		q.execute_query(query_add)
		queries.append(query_add)
	query_supplier = "select id, name from deliveryapp_supplier where is_deleted <> 1"
	query_product = "select id, category from deliveryapp_product where is_deleted <> 1"
	query_bill = "select id, bill_number from deliveryapp_bill where is_deleted <> 1"
	bills = list(q.execute_query(query_bill))
	suppliers = list(q.execute_query(query_supplier))
	products = list(q.execute_query(query_product))
	queries.append(query_bill)
	queries.append(query_supplier)
	queries.append(query_product)
	purchases = list(q.execute_query("select id from deliveryapp_purchase"))
	queries.append("select id from deliveryapp_purchase")
	return render(request,"purchases.html",{'queries':queries, 'purchases':purchases,'suppliers':suppliers, 'products':products,'bills':bills})

def delivery(request, id):
	queries = [] 
	delivery = list(q.execute_query("select driver_in_id, driver_out_id,location_from_id, location_to_id,customer_id from\
							  deliveryapp_delivery where id = {0}".format(str(id))))[0]
	queries.append("select driver_in_id, driver_out_id,location_from_id, location_to_id,customer_id from\
							  deliveryapp_delivery where id = {0}".format(str(id)))
	driver_in_id = delivery[0]
	driver_out_id = delivery[1]
	location_from_id = delivery[2]
	location_to_id = delivery[3]
	customer_id = delivery[4]
	customer_name = list(q.execute_query("select name from deliveryapp_customer where id = {0}".format(customer_id)))[0][0]
	driver_in_name = list(q.execute_query("select name from deliveryapp_delivery_man where id = {0}".format(driver_in_id)))[0][0]
	driver_out_name = list(q.execute_query("select name from deliveryapp_delivery_man where id = {0}".format(driver_out_id)))[0][0]
	queries.append("select name from deliveryapp_customer where id = {0}".format(customer_id))
	queries.append("select name from deliveryapp_delivery_man where id = {0}".format(driver_in_id))
	queries.append("select name from deliveryapp_delivery_man where id = {0}".format(driver_out_id))
	return render(request, "delivery.html", {'pk':id,'customer_name':customer_name,'driver_in_name':driver_in_name, 'driver_out_name':driver_out_name,'customer_name':customer_name,'queries':queries,'delivery_in_id':driver_in_id, 'delivery_out_id':driver_out_id, 'location_from_id':location_from_id,'location_to_id':location_to_id,'customer_id':customer_id})



def purchase(request,id):
	queries = []
	purchase  = list(q.execute_query("select quantity, supplier_id, product_id, bill_id from deliveryapp_purchase where id = {0}".format(str(id))))[0]
	queries.append("select id, quantity, supplier_id, product_id, bill_id from deliveryapp_purchase where id = {0}".format(str(id)))
	quantity = purchase[0]
	supplier_id  = purchase[1]
	product_id  = purchase[2]
	bill_id = purchase[3]
	supplier_name = list(q.execute_query("select name from deliveryapp_supplier where id = {0} ".format(supplier_id)))[0][0]
	bill_number = list(q.execute_query("select bill_number from deliveryapp_bill where id = {0} ".format(bill_id)))[0][0]
	product_category = list(q.execute_query("select category from deliveryapp_product where id = {0} ".format(product_id)))[0][0]
	queries.append("select name from deliveryapp_supplier where id = {0} ".format(supplier_id))
	queries.append("select bill_number from deliveryapp_bill where id = {0} ".format(bill_id))
	queries.append("select category from deliveryapp_product where id = {0} ".format(product_id))
	return render(request, "purchase.html",{'quantity':quantity,'pk':id, 'supplier_name':supplier_name,'product_category':product_category,'bill_number':bill_number,'queries':queries})


	bill_number=models.IntegerField(null=False,unique=True,max_length=30)
	id=models.IntegerField(null=False,primary_key=True)
	delivery_charge=models.PositiveIntegerField(default=0)
	date=models.DateField(default='none',max_length=30)
	delivery=models.ForeignKey(Delivery,on_delete=models.DO_NOTHING)
	manager=models.ForeignKey(Manager,on_delete=models.DO_NOTHING)
	status=models.CharField(max_length=99, choices=Status_Choices, default="pending" )
	is_deleted=models.BooleanField(default=False)

def bill(request,id):
	queries= []
	bill = list(q.execute_query("select date, delivery_id, manager_id,status, bill_number status from deliveryapp_bill where id = {0} ".format(id)))[0]
	queries.append("select date, delivery_id, manager_id, status, bill_number from deliveryapp_bill where id = {0} ".format(id))
	date = bill[0]
	delivery_id = bill[1]
	manager_id = bill[2]
	status = bill[3]
	bill_number = bill[4]
	manager_name = list(q.execute_query("select name from deliveryapp_manager where id = {0}".format(manager_id)))[0][0]
	queries.append("select name from deliveryapp_manager where id = {0}".format(manager_id))
	total_product_price = list(q.execute_query(q.GET_TOTAL_BILL_CHARGE.format(id)))[0][0]
	total_product_mass = list(q.execute_query(q.GET_TOTAL_BILL_MASS.format(id)))[0][0]
	queries.append(q.GET_TOTAL_BILL_CHARGE.format(id))
	queries.append(q.GET_TOTAL_BILL_MASS.format(id))
	return render(request,"bill.html", {'pk':id,'bill_number':bill_number, 'queries':queries,'total_product_mass':total_product_mass,'manager_name':manager_name, 'status':status, 'delivery_id':delivery_id,'date':date, 'total_product_price':total_product_price})



