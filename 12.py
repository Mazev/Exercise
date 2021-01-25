gifts = input().split()

command = input()
while not command == 'No Money':
    word = command.split()
    if word[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == word[1]:
                gifts[i] = 'None'
            if i != word[1]:
                continue
    if word[0] == 'Required':
        if int(word[2]) > len(gifts):
            break
        elif int(word[2]) <= len(gifts):
            gifts[int(word[2])] = word[1]
    if word[0] == 'JustInCase':
        gifts.pop(-1)
        gifts.append(word[1])
    command = input()

for i in gifts:
    if i == 'None':
        gifts.remove(i)

print(*gifts)