number = int(input())

parking_data = {}


for _ in range(number):
    command = input().split()
    token = command[0]
    if token == 'register':
        username = command[1]
        plate = command[2]
        if username not in parking_data:
            parking_data[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif token == 'unregister':
        username = command[1]
        if username not in parking_data:
            print(f"ERROR: user {username} not found")
        else:
            parking_data.pop(username)
            print(f"{username} unregistered successfully")

for username, plate in parking_data.items():
    print(f'{username} => {plate}')
