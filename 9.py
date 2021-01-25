numbers = input().split(', ')
beggars_count = int(input())

money = []

for n in numbers:
    n = int(n)
    money.append(n)

beggars = []
for count in range(beggars_count):
    beggars.append(0)

index = 0
for num in money:
    beggars[index] += num
    index += 1

    if index == beggars_count:
        index = 0

print(beggars)



