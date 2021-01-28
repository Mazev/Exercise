wagons = int(input())

list_wagons = [0] * wagons

token = input()
while not token == 'End':
    command = token.split()

    if command[0] == 'add':
        number_of_people = int(command[1])
        list_wagons[-1] += number_of_people
    elif command[0] == 'insert':
        index = int(command[1])
        number_of_people = int(command[2])
        list_wagons[index] += number_of_people
    elif command[0] == 'leave':
        index = int(command[1])
        number_of_people = int(command[2])
        list_wagons[index] -= number_of_people

    token = input()

print(list_wagons)
