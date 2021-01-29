string_1 = input().split(', ')
string_2 = input().split(', ')

new_list = []

for el in string_1:
    for i in string_2:
        if el in i and el not in new_list:
            new_list.append(el)

print(new_list)