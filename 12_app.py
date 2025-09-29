



from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

app = Flask(__name__)

DB_NAME = "inventory.db"

#Database Setup
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY(order_id) REFERENCES orders(id),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ------------------- Home -------------------
@app.route("/")
def home():
    return render_template("home.html")

# ------------------- Products -------------------
@app.route("/products")
def products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    conn.close()
    return render_template("products.html", products=products)

@app.route("/add_product", methods=["POST"])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()
    return redirect(url_for('products'))

# ------------------- Customers -------------------
@app.route("/customers")
def customers():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    customers = cur.fetchall()
    conn.close()
    return render_template("customers.html", customers=customers)

@app.route("/add_customer", methods=["POST"])
def add_customer():
    name = request.form['name']
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO customers (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for('customers'))

# ------------------- Orders -------------------
@app.route("/orders")
def orders():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT orders.id, customers.name, orders.date FROM orders LEFT JOIN customers ON orders.customer_id = customers.id")
    orders = cur.fetchall()
    conn.close()
    return render_template("orders.html", orders=orders)

@app.route("/add_order", methods=["POST"])
def add_order():
    customer_id = request.form['customer_id']
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (customer_id) VALUES (?)", (customer_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('orders'))

# ------------------- Templates -------------------
# Save these in a folder called 'templates' in the same directory as app.py

# home.html
"""
<!DOCTYPE html>
<html>
<head><title>Inventory System</title></head>
<body>
    <h1>Inventory Management</h1>
    <a href="/products">Products</a> | 
    <a href="/customers">Customers</a> | 
    <a href="/orders">Orders</a>
</body>
</html>
"""

# products.html
"""
<!DOCTYPE html>
<html>
<head><title>Products</title></head>
<body>
    <h1>Products</h1>
    <form method="POST" action="/add_product">
        Name: <input type="text" name="name" required>
        Price: <input type="number" step="0.01" name="price" required>
        Stock: <input type="number" name="stock" required>
        <button type="submit">Add</button>
    </form>
    <ul>
    {% for p in products %}
        <li>{{p[1]}} - ${{p[2]}} (Stock: {{p[3]}})</li>
    {% endfor %}
    </ul>
    <a href="/">Home</a>
</body>
</html>
"""

# customers.html
"""
<!DOCTYPE html>
<html>
<head><title>Customers</title></head>
<body>
    <h1>Customers</h1>
    <form method="POST" action="/add_customer">
        Name: <input type="text" name="name" required>
        <button type="submit">Add</button>
    </form>
    <ul>
    {% for c in customers %}
        <li>{{c[1]}}</li>
    {% endfor %}
    </ul>
    <a href="/">Home</a>
</body>
</html>
"""

# orders.html
"""
<!DOCTYPE html>
<html>
<head><title>Orders</title></head>
<body>
    <h1>Orders</h1>
    <form method="POST" action="/add_order">
        Customer ID: <input type="number" name="customer_id" required>
        <button type="submit">Create Order</button>
    </form>
    <ul>
    {% for o in orders %}
        <li>Order #{{o[0]}} by {{o[1]}} at {{o[2]}}</li>
    {% endfor %}
    </ul>
    <a href="/">Home</a>
</body>
</html>
"""

# ------------------- Run -------------------
if __name__ == "__main__":
    app.run(debug=True)