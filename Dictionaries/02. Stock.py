products = input().split()

dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    dict[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in dict:
        print(f"We have {dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
