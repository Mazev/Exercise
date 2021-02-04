command = input()
dict = {}
while command != 'stop':
    type = command
    resource = int(input())
    if not type in dict:
        dict[command] = resource
    else:
        dict[type] += resource

    command = input()

for key, value in dict.items():
    print(f'{key} -> {value}')
