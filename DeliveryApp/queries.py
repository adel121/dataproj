import sqlite3
GET_ALL_DATA  = "select * from deliveryapp_{0}"
GET_DATA_BY_ATTR=  "select * from deliveryapp_{0} where '{1}'='{2}'" 
GET_DATA_BY_ATTRS= "select * from deliveryapp_{0} where '{1}'='{2}' '{3}' '{4}'='{5}'"
INSERT= "insert into deliveryapp_{0}"
GET_BILLS_BY_BILL_NUMBER="select * from deliveryapp_bill where bill_number LIKE '*{0}*' "
GET_BILL_BY_DATE_RANGE_FOR_SUPPLIER ="select deliveryapp_bill.bill_number from \
									(deliveryapp_bill as b INNER JOIN deliveryapp_purchase as p ON\
									p.bill = b.id and b.date <= '{0}'' and b.date >= '{1}'')\
									INNER JOIN deliveryapp_supplier as s ON\
						 			p.supplier = s.id where s.name = '{2}'"				
GET_CUSTOMER_BY_TEL_NUMBER="select * from deliveryapp_customer where tel_num LIKE '*{0}*' "
GET_BILLS_BY_TEL_NUM="select deliveryapp_bill.bill_number from (deliveryapp_bill as b INNER JOIN \
					  deliveryapp_delivery as d ON b.delivery = d.id)\
					  INNER JOIN deliveryapp_customer as c ON (c.id=d.customer and c.tel_num LIKE '*{0}*')"
GET_UNFINALIZED_BILLS_FOR_SUPPLIER = " select deliveryapp_bill.bill_number from \
									   deliveryapp_bill as b INNER JOIN deliveryapp_purchase as p \
									   ON p.bill = b.id and b.status <> 'finalized' INNER JOIN deliveryapp_supplier as s ON\
									   p.supplier = s.id and s.name = '{0}'"
GET_UNFINALIZED_BILLS_FOR_CUSTOMER ="select deliveryapp_bill.bill_number from (deliveryapp_bill as b INNER JOIN \
					 				 deliveryapp_delivery as d ON b.delivery = d.id and b.status <> 'finalized')\
								     INNER JOIN deliveryapp_customer as c ON (c.id=d.customer and c.name= '{0}')"
GET_UNFINALIZED_BILLS_FOR_DRIVER_MAN ="select deliveryapp_bill.bill_number from (deliveryapp_bill as b INNER JOIN \
					 				 deliveryapp_delivery as d ON b.delivery = d.id and b.status <> 'finalized')\
								     INNER JOIN deliveryapp_driver_man as m ON ((m.id=d.driver_in) or (m.id=d.driver_out)\
								     and m.name='{0}')"

GET_SORTED_SUPPLIERS_WITHIN_DATE_RANGE = "select COUNT(bill_id) as freq, name \
										from (deliveryapp_purchase as p INNER JOIN deliveryapp_bill as b ON p.bill_id=b.id \
										and b.date >= '{0}' and b.date <= '{1}' INNER JOIN deliveryapp_supplier as s ON \
										p.supplier_id = s.id) GROUP BY name \
										ORDER BY COUNT(bill_id) DESC"

GET_DELOUT_COUNT_FOR_DRIVER_WITHIN_DATE_RANGE="select COUNT(*) as freq_out from deliveryapp_bill as b INNER JOIN \
					 				 			 deliveryapp_delivery as d ON b.delivery_id = d.id and b.date >= '{0}' \
					 				 			 and b.date <= '{1}' INNER JOIN deliveryapp_delivery_man as dr ON dr.id \
					 				 			 = d.driver_out_id and dr.name='{2}'"

GET_DELIN_COUNT_FOR_DRIVER_WITHIN_DATE_RANGE="select COUNT(*) as freq_out from deliveryapp_bill as b INNER JOIN \
					 				 			 deliveryapp_delivery as d ON b.delivery_id = d.id and b.date >= '{0}' \
					 				 			 and b.date <= '{1}' INNER JOIN deliveryapp_delivery_man as dr ON dr.id \
					 				 			 = d.driver_in_id and dr.name='{2}'"

 

GET_DEST_COUNT_FOR_DRIVER_WITHIN_DATE_RANGE= "select COUNT(DISTINCT location_to_id) from deliveryapp_bill as b\
											  INNER JOIN deliveryapp_delivery as d ON b.date >= '{0}' and b.date <= '{1}'\
											  INNER JOIN deliveryapp_delivery_man as dr ON\
											  d.driver_out_id = dr.id and dr.name= '{2}' "

GET_TOTAL_BILL_CHARGE="select SUM(total) from (select ( quantity * unit_price ) as total from\
					   (select product_id, quantity from \
					   deliveryapp_purchase as p where p.bill_id = '{0}') INNER JOIN deliveryapp_product as pr ON\
					   product_id = pr.id)"

GET_TOTAL_BILL_MASS="select SUM(total) from (select ( quantity * unit_mass ) as total from\
					   (select product_id, quantity from \
					   deliveryapp_purchase as p where p.bill_id = '{0}') INNER JOIN deliveryapp_product as pr ON\
					   product_id = pr.id)"					   

def INSERT_AUX(attrs, values):
	temp = '('
	for attr in attrs:
		temp = temp + attr  + ','
	temp = temp[:len(temp)-1]+") values("
	for value in values:
		temp = temp + value  + ','
	temp = temp[:len(temp)-1]+");"
	return temp


def execute_query(query):
	connection=sqlite3.connect('db.sqlite3')
	cursor=connection.cursor()
	print(query)
	res = cursor.execute(query)
	connection.commit()
	return res
