products = ("laptop", "mobile", "tablet")

item = input("Enter product name: ")

if item in products:
    print("Product available")
else:
    print("Not available")
