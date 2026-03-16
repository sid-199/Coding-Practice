items = []
prices = []

n = int(input("How many items? "))

for i in range(n):
    item = input(f"Enter item {i+1}: ")
    price = float(input(f"Enter price of {item}: "))
    items.append(item)
    prices.append(price)

print("\nItemized List:")
print(dict(zip(items,prices)))

print(f"\nTotal cost: ₹{sum(prices)}")
sid=dict(zip(items,prices))

ans=[key for key in sid if sid[key] > 20 ]


print(ans)

with open("price.txt","w") as f:
    f.write("\n List of all items")
    for item, price in sid.items():
        f.write(f"\n{item}- Rs{price}")
