json_body = {
  "user": {
    "id": "u1001",
    "name": "Alice",
    "email": "alice@example.com",
    "active": True
  },
  "product": {
    "id": "p2001",
    "name": "Laptop",
    "price": 1200.00,
    "in_stock": 15
  }
}

# Access the user name
user_name = json_body["user"]["name"]
user_name = json_body.get("user",{}).get("name","")
print(user_name)

product_price = json_body["product"]["price"]
print(product_price)

# Check User Active Status
user_status = json_body.get("user",{}).get("active")
print(user_status)

# Access Product ID: 
product_id = json_body.get("product",{}).get("id","")
print(product_id)

# List Top-Level Keys
print(json_body.keys())
