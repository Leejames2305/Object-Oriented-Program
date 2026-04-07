# ========== Assesment 2 ==========
# Student Name 1    : Lee Xin Yi
# Student ID 1      : 2103307
# Student Programme : MH
#  
# Student Name 2    : Chua Yun Juan
# Student ID 2      : 2103232
# Student Programme : MH
# ====================================

# Base Class: Order
class Order:
    def __init__(self, order_id, customer_name, order_type, price, distance=0):
        self._order_id = order_id
        self._customer_name = customer_name
        self._order_type = order_type
        self._price = float(price)
        self._distance = float(distance)

    def calculate_price(self):
        return self._price
    
    def get_summary(self):
        price = self.calculate_price()
        return (f"{self._customer_name} ({self._order_type}) - Distance: {self._distance} km, "
                f"Final Price: RM {price:,.2f}")

# Subclass: PickupOrder (Behave same as Order, without delivery fee)
class PickupOrder(Order):
    def __init__(self, order_id, customer_name, price, distance=0):
        super().__init__(order_id, customer_name, "Pickup", price, distance)

    def get_summary(self):  # Override base method to exclude distance for Pickup orders
        return (f"{self._customer_name} ({self._order_type}) - "
                f"Final Price: RM {self.calculate_price():,.2f}")

# Subclass: DeliveryOrder (Behave same as Order, with delivery fee based on distance ; RM 1.5 per km, minimum RM 5)
class DeliveryOrder(Order):
    def __init__(self, order_id, customer_name, price, distance):
        super().__init__(order_id, customer_name, "Delivery", price, distance)

    def calculate_delivery_fee(self):
        return max(5, self._distance * 1.5)

    def calculate_price(self):  # Override base method to include get total price with delivery
        delivery_fee = self.calculate_delivery_fee()
        return self._price + delivery_fee
    
    def distance_category(self):  # Categorize order based on distance
        if self._distance < 4:
            return "Nearby"
        elif 4 <= self._distance < 8:
            return "Short Distance"
        elif 8 <= self._distance < 12:
            return "Medium Distance"
        else:
            return "Long Distance"

def load_data(file_path):
    orders = []
    with open(file_path, 'r') as file:
        next(file)  # Skip header
        for line in file:
            order_id, customer_name, order_type, price, distance = line.strip().split(',')
            if order_type == "Pickup":
                orders.append(PickupOrder(order_id, customer_name, price))
            elif order_type == "Delivery":
                orders.append(DeliveryOrder(order_id, customer_name, price, distance))
    return orders

def delivery_statistics_by_distance_category(orders):
    categories = {"Long Distance": [], "Medium Distance": [], "Short Distance": [], "Nearby": []}
    for order in orders:
        if isinstance(order, DeliveryOrder):  # Only consider delivery orders for distance categories
            filteredCategory = order.distance_category()
            categories[filteredCategory].append(order.calculate_delivery_fee())  # Append delivery fee to the respective category list
    
    print("Delivery Statistics by Distance Category:")
    for category, delivery_fees in categories.items():
        if delivery_fees:  # Only calculate if there is at least one order in the category
            average_delivery_fees = sum(delivery_fees) / len(delivery_fees)
            print(f"{category}")
            print(f"Total Orders = {len(delivery_fees)}")
            print(f"Average Delivery Price = RM {average_delivery_fees:,.2f}")
            print()
        else:
            print(f"{category}: No orders")

def top_3_customers_by_spending(orders):
    customer_spending = {}
    for order in orders:
        customer_spending[order._customer_name] = customer_spending.get(order._customer_name, 0) + order.calculate_price()
    
    top_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]  # Sort customers and get only top 3
    i = 1
    print("\nTop 3 Customers by Total Spending:")
    for customer, total in top_customers:
        print(f"{i:>2}. {customer:<10} - RM {total:>6,.2f}")
        i += 1

def get_order_by_id(orders, order_id):
    for order in orders:  # Loop through and find matching order ID
        if order._order_id == order_id:
            print(f"\nOrder Summary:")
            print(order.get_summary())
            return
    print(f"\nInvalid Order: {order_id}")


#### Main Execution ####
orders = load_data("Practical_7/Assessment_2/oop_food_orders.csv")
delivery_statistics_by_distance_category(orders)
top_3_customers_by_spending(orders)
get_order_by_id(orders, "O001")
get_order_by_id(orders, "O002")
get_order_by_id(orders, "O999")
get_order_by_id(orders, "O009")