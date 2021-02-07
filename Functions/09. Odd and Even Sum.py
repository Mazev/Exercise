number = (input())


def odd_and_even_sum(num):
    odd_sum = []
    even_sum = []
    for el in num:
        el = int(el)
        if el % 2 == 0:
            even_sum.append(el)
        else:
            odd_sum.append(el)
    print(f'Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}')


odd_and_even_sum(number)
