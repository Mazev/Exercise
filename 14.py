collection_items = input().split('|')
budget = int(input())

new_price_items = []
profit = []
for item in collection_items:
    type, price = item.split('->')
    price = float(price)
    if budget < price:
        break
    if type == 'Clothes':
        if price <= 50:
            budget -= price
            profit_items = price * 0.40
            profit.append(profit_items)
            price += price * 0.40
            new_price_items.append(price)
    elif type == 'Shoes':
        if price <= 35:
            budget -= price
            profit_items = price * 0.40
            profit.append(profit_items)
            price += price * 0.40
            new_price_items.append(price)
    elif type == 'Accessories':
        if price <= 20.50:
            budget -= price
            profit_items = price * 0.40
            profit.append(profit_items)
            price += price * 0.40
            new_price_items.append(price)

need_money = 150
for el in new_price_items:
    print(f'{el:.2f}', end=' ')
print()
print(f'Profit: {sum(profit):.2f}')

if sum(new_price_items) + budget > need_money:
    print('Hello, France!')
else:
    print('Time to go.')
