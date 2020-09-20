price =float(input("What is the item's price? "))

if price <= 9.99:
    shippingCost = 5.95
    print("Your shipping cost is $5.95.")
elif price <= 29.99:
    shippingCost = 7.95
    print("Your shipping cost is $7.95")
elif price <= 49.99:
    shippingCost = 11.95
    print("Your shipping cost is $11.95.")
else:
    shippingCost = 0.00
    print("Because your order is over $50, the shipping is free!")


cash_coupon =float(input("What is your dollar discount? "))
percent_coupon = float(input("What is your percentage off in decimal form? "))
taxRate = 0.06

calculate_price = (((price - cash_coupon) - (price * percent_coupon) + (price * taxRate )) + shippingCost)
calculate_price_float = "{:.2f}".format(calculate_price)
print("Your total to pay today after discounts, tax, and shipping is: ")
print(calculate_price_float)
