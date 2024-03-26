class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

class OrderCostCalculator:
    def calculate_total_cost(self, items):
        total_cost = 100
        return total_cost
    
class OrderValidator:
    def validate_order(self, order_info):
        is_valid = True
        return is_valid

class OrderEmailSender:
    def send_confirmation_email(self, customer_email):
        print (f"Confirmation email sent to {customer_email}")

class InventoryUpdater:
    def update_inventory(self, processed_items):
        print(f"Inventory updated for items: {processed_items}")    
