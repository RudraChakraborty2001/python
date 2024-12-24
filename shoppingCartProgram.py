item = input("What item would you like to bye? ")
price = float(input("What is the price? "))
quantity = int(input("How mane would you like? "))
total_price = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"You total is : {total_price}")
