num_items = int(input("Number of items: "))
totalPrice = 0.0
for i in range (1, num_items+1):
    curItem_price = float(input("Price of Item #" + str(i) + ": "))
    totalPrice += curItem_price
print("Total price for " + str(num_items) + " items is $" + str(totalPrice))
