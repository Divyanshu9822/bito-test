from datetime import datetime

class OrderService:
    def __init__(self):
        self.orders = []
    
    def add_order(self, product):
        new_order = {
            'order_id': len(self.orders) + 1,
            'product': product,
            'order_date': datetime.now()
        }
        self.orders.append(new_order)
        from utils.dateUtils import format_date
        formatted_date = format_date(new_order['order_date'], 'DD-MM-YYYY')
        print(f"Order Added: {new_order['product']}, Order Date: {formatted_date}")

    def list_orders(self):
        for order in self.orders:
            formatted_date = format_date(order['order_date'])
            print(f"Order ID: {order['order_id']}, Product: {order['product']}, Order Date: {formatted_date}")
\ No newline at end of file