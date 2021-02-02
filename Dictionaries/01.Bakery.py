some_food = input().split()

bakery = {}

for i in range(0, len(some_food), 2):
    key = some_food[i]
    value = some_food[i +1]
    bakery[key] = int(value)
print(bakery)