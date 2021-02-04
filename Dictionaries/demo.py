# my_hero = superhero_dict.get('dark_horse_hero', 'Этот ключ в словаре отсутствует!')
# print(my_hero)


# statistic_dict = {'b': 13, 'd': 30, 'e': -32, 'c': 93, 'a': 33}
# for key in sorted(statistic_dict):
#     print(key)


# elements = {'el1': 1, 'el2': 0, 'el3': -2, 'el4': 95, 'el5': 13}
# elements_sorted = {k: elements[k] for k in sorted(elements, key=elements.get, reverse= False)}
# print(elements_sorted)


# my_dict = {'name':'Jack', 'age': 26}
# my_dict['age'] = 27
# my_dict['name'] = 'stefan'
# print(my_dict['name'])
# print(my_dict['age'])


# n = input().split()
#
# bakery = {}
#
# for i in range(0, len(n), 2):
#     key = n[i]
#     value = n[i + 1]
#     bakery[key] = int(value)
#
# print(bakery)

# n = input().split()
#
# bakery = {}
#
# for i in range(0, len(n), 2):
#     key = n[i]
#     value = n[i + 1]
#     bakery[key] = int(value)
#
# for key in bakery.keys():
#     print(key)


# dict = {1: 1, 2: 4, 3: 9}
# for key in dict.keys():
#     dict[key] **= 2
# print(dict)

# for value in dict.values():
#     print(value, end = ' ')

# for key in dict.keys():
#     print(dict[key])

# for key, value in dict.items():
#     print(f'Key: {key}, Value: {value}', end = ' ')


# numbers = {1: 'one', 2: 'two'}
# for el in numbers:
#     print(el)

# for key, value in numbers.items():
#     print(key, value)
#
# if 'one' in numbers.values():
#     print('oe')
# else:
#     print('no')