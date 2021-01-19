num = input().split()

new_list = []

for el in num:
    el = int(el)
    el *= -1
    new_list.append(el)
print(new_list)