'''
get number of items
while item number < 0:
print invalid
get number of items
for i in range
get price
get total price
print item number and total price
'''

price = 0
total_price = 0
items = int(input("Number of items: "))
while items < 0:
    print ("invalid number of items!")
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    final_price = total_price * 0.9
print("Total price for {} items is ${:.2f}".format(items, final_price))

