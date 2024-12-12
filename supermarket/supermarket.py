class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.initial_quantity = quantity
        self.sold_quantity = 0

    def __str__(self):
        return f"{self.name} - Price: {self.price:.2f}, Quantity: {self.quantity}"


class SupermarketInventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name].quantity += quantity
            self.items[name].initial_quantity += quantity
            print(f"Updated {name}: New Quantity = {self.items[name].quantity}")
        else:
            self.items[name] = InventoryItem(name, price, quantity)
            print(f"Added {name} to the inventory.")

    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item in self.items.values():
                print(item)

    def display_available_items(self):
        available_items = [item for item in self.items.values() if item.quantity > 0]
        if not available_items:
            print("No items available in the inventory.")
        else:
            print("Available Items:")
            for item in available_items:
                print(item)

    def customer_purchase(self, item_name, quantity):
        if item_name not in self.items:
            print(f"Error: {item_name} is not available in the inventory.")
            return

        item = self.items[item_name]

        if item.quantity < quantity:
            print(f"Error: Insufficient stock for {item_name}. Available Quantity: {item.quantity}")
            return
        total_cost = item.price * quantity
        item.quantity -= quantity 
        item.sold_quantity += quantity  

        print(f"Purchased {quantity} of {item_name}. Total Cost: ₹{total_cost:.2f}")
        print(f"Remaining Quantity of {item_name}: {item.quantity}")

    def sales_analysis_report(self):
        if not self.items:
            print("No items in the inventory for analysis.")
            return
        print("\n--- Sales Analysis Report ---")
        total_sold = sum(item.sold_quantity for item in self.items.values())
        total_initial = sum(item.initial_quantity for item in self.items.values())
        percentage_sold = (total_sold / total_initial) * 100 if total_initial > 0 else 0
        most_sold = max(self.items.values(), key=lambda x: x.sold_quantity, default=None)
        least_sold = min(self.items.values(), key=lambda x: x.sold_quantity, default=None)
        print(f"Percentage of Items Sold: {percentage_sold:.2f}%")
        if most_sold:
            print(f"Most Sold Product: {most_sold.name} ({most_sold.sold_quantity} units sold)")
        if least_sold:
            print(f"Least Sold Product: {least_sold.name} ({least_sold.sold_quantity} units sold)")




