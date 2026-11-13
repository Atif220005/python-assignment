Customer_name = "Enter the name of customer: "

product_1 = input("Enter product name: ")
price_1 = int(input("Enter price: "))

product_2 = input("Enter product name: ")
price_2 = int(input("Enter price: "))

product_3 = input("Enter product name: ")
price_3 = int(input("Enter price: "))

Total = price_1 + price_2 + price_3

if Total > 4999:
    discount_rate = 0.20
elif Total > 2999: 
    discount_rate = 0.10
elif Total > 999:
    discount_rate = 0.5
else:
    discount_rate = 0

Discount = Total * discount_rate

Final_Total = Total - Discount

print(f"Product 1 {product_1}")
print(f"Price: {price_1}")

print(f"Product 2 {product_2}")
print(f"Price: {price_2}")

print(f"Product 3 {product_3}")
print(f"Price: {price_3}")

print(f"Subtotal: {Total}")
print(f"Discount: {Discount}")
print(f"Final Total: {Final_Total}")