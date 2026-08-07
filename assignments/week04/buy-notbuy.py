prices = []

print("Enter prices of 6 items:")

for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

print()

budget = int(input("Enter total budget: "))
print()

total = 0
bought_items = []

for i in range(6):
    if total + prices[i] <= budget:
        print(f"Item {i + 1} = {prices[i]} --> buy")
        total += prices[i]
        bought_items.append(prices[i])
    else:
        print(f"Item {i + 1} = {prices[i]} --> cannot buy")

    print(f"Current total = {total}")
    print()

print(f"Bought items: {bought_items}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")