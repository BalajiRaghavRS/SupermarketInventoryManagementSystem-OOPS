from supermarket import *

inventory = SupermarketInventory()


inventory.add_item("Apples", 50.0, 30)
inventory.add_item("Bananas", 20.0, 50)
inventory.add_item("Milk", 60.0, 10)


inventory.customer_purchase("Apples", 10)
inventory.customer_purchase("Milk", 5)
inventory.customer_purchase("Bananas", 20)


inventory.sales_analysis_report()