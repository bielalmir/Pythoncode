import datetime
import sys
from collections import Counter

inventory = {
    "Apple": {
        "iPhone 12": {"price": 25000, "stock": 100},
        "iPhone 13": {"price": 45000, "stock": 700},
        "iPhone 14": {"price": 55000, "stock": 500},
        "iPhone 15": {"price": 65000, "stock": 300},
        "iPhone 16": {"price": 110000, "stock": 200}
    },
    "Samsung": {
        "S21": {"price": 55000, "stock": 800},
        "S22": {"price": 65000, "stock": 699},
        "S23": {"price": 75000, "stock": 599},
        "S24": {"price": 80000, "stock": 489},
        "S25": {"price": 85000, "stock": 387}
    },
    "JAVA": {
        "A1": {"price": 5000, "stock": 157},
        "A2": {"price": 6000, "stock": 127},
        "A3": {"price": 7000, "stock": 105},
        "A4": {"price": 8000, "stock": 634},
        "A5": {"price": 9000, "stock": 534}
    },
    "Nokia": {
        "Nokia 3310": {"price": 2500, "stock": 203},
        "Nokia Lumia": {"price": 15000, "stock": 822},
        "Nokia X20": {"price": 20000, "stock": 644},
        "Nokia Gt": {"price": 18000, "stock": 543}
    },
    "Micromax": {
        "Micromax A1": {"price": 5000, "stock": 104},
        "Micromax B2": {"price": 7000, "stock": 834},
        "Micromax InNote": {"price": 12000, "stock": 634},
        "Micromax Infinity": {"price": 15000, "stock": 445}
    }
}

#  ORDER & SALES DATA
orders = []   #store all orders

#FUNCTIONS
def show_brands():
    print("\n Available Brands:")
    for brand in inventory:
        print("-", brand)

def show_items(brand):
    if brand in inventory:
        print(f"\n {brand} Mobiles:")
        for model, data in inventory[brand].items():
            stock_status = " Low Stock!" if data["stock"] < 5 else ""
            print(f"{model} : ₹{data['price']} | Stock: {data['stock']} {stock_status}")
    else:
        print(" Brand not found!")

def search_model(model_name):
    print(f"\n Search Results for '{model_name}':")
    found = False
    for brand, models in inventory.items():
        for model, data in models.items():
            if model_name.lower() in model.lower():
                print(f"{brand} - {model}: ₹{data['price']} | Stock: {data['stock']}")
                found = True
    if not found:
        print(" No model found!")

def place_order(customer_name, brand, model, quantity):
    if brand in inventory and model in inventory[brand]:
        item = inventory[brand][model]
        if item["stock"] < quantity:
            print(" Not enough stock available!")
            return

        price = item["price"]
        total = price * quantity

        # Apply discount for bulk orders
        discount = 0
        if quantity >= 3:
            discount = 0.1  # 10% discount
            total = total - (total * discount)

        # Update stock
        item["stock"] -= quantity

        order = {
            "customer": customer_name,
            "brand": brand,
            "model": model,
            "quantity": quantity,
            "total": total,
            "date": datetime.date.today()
        }
        orders.append(order)

        print(f"\n Order placed successfully for {model} x{quantity}")
        if discount:
            print(f" Discount Applied: 10% OFF")
        print(f" Total Bill: ₹{total}")
    else:
        print(" Mobile not available!")

def customers_today():
    today = datetime.date.today()
    cust = {o["customer"] for o in orders if o["date"] == today}
    print("\n Customers Today:", ", ".join(cust) if cust else "No customers yet.")

def items_today():
    today = datetime.date.today()
    items = [o["model"] for o in orders if o["date"] == today]
    print("\n Items Sold Today:", ", ".join(items) if items else "No items sold today.")

def most_sold():
    all_items = [o["model"] for o in orders]
    if all_items:
        most = Counter(all_items).most_common(1)[0]
        print(f"\n Most Sold Item: {most[0]} (Sold {most[1]} times)")
    else:
        print("\n No sales yet!")

def sales_summary_today():
    today = datetime.date.today()
    total_sales = sum(o["total"] for o in orders if o["date"] == today)
    print(f"\n Total Sales Today: ₹{total_sales}")

def report(start_date, end_date):
    print(f"\n Orders Report ({start_date} → {end_date}):")
    filtered = [o for o in orders if start_date <= o["date"] <= end_date]
    if not filtered:
        print("No orders in this period.")
        return
    for o in filtered:
        print(f"{o['date']} | {o['customer']} | {o['brand']} {o['model']} x{o['quantity']} | ₹{o['total']}")

def view_all_orders():
    print("\n All Orders History:")
    if not orders:
        print("No orders yet.")
        return
    for o in orders:
        print(f"{o['date']} | {o['customer']} | {o['brand']} {o['model']} x{o['quantity']} | ₹{o['total']}")

# --------- MAIN MENU ---------
def main():
    while True:
        print("\n==========  Mobile Shop Inventory System ==========")
        print("1. Show Brands")
        print("2. Show Items by Brand")
        print("3. Search Mobile")
        print("4. Place an Order")
        print("5. Customers Today")
        print("6. Items Sold Today")
        print("7. Most Sold Item")
        print("8. Sales Summary Today")
        print("9. Report of Orders")
        print("10. View All Orders")
        print("11. Exit")
        print("=====================================================")

        choice = input("Enter choice: ")

        if choice == "1":
            show_brands()
        elif choice == "2":
            brand = input("Enter Brand: ")
            show_items(brand)
        elif choice == "3":
            model_name = input("Enter Model Name: ")
            search_model(model_name)
        elif choice == "4":
            customer = input("Enter Customer Name: ")
            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            qty = int(input("Enter Quantity: "))
            place_order(customer, brand, model, qty)
        elif choice == "5":
            customers_today()
        elif choice == "6":
            items_today()
        elif choice == "7":
            most_sold()
        elif choice == "8":
            sales_summary_today()
        elif choice == "9":
            s = input("Enter Start Date (YYYY-MM-DD): ")
            e = input("Enter End Date (YYYY-MM-DD): ")
            start_date = datetime.date.fromisoformat(s)
            end_date = datetime.date.fromisoformat(e)
            report(start_date, end_date)
        elif choice == "10":
            view_all_orders()
        elif choice == "11":
            print(" Exiting... Thank you for using Mobile Shop System!")
            sys.exit()
        else:
            print(" Invalid Choice! Please try again.")

# --------- RUN ---------
if __name__ == "__main__":
    main()

