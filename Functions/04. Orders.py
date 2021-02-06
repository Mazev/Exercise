product = input()
quantity = int(input())


def orders(order, number):
    if order == 'coffee':
       return number * 1.50
    elif order == 'water':
        return number * 1.00
    elif order == ' coke':
        return number * 1.40
    elif order == 'snacks':
        return number * 2.00


print(f'{orders(product, quantity):.2f}')
