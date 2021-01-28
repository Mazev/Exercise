command = input()
notes = [0]* 100

while not command == 'End':
    tokens = command.split('-')
    priority = int(tokens[0])
    value = tokens[1]
    notes.insert(priority, value)

    command = input()

new_list = []
for el in notes:
    if el != 0:
        new_list.append(el)
print(new_list)
