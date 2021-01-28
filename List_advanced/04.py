numbers = list(map(lambda x: int(x), input().split(', ')))

even_num = []

for num in range(len(numbers)):
    if numbers[num] % 2 == 0:
        even_num.append(num)

print(even_num)