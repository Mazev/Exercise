dungeons_room = input().split('|')

curent_health = 100
bitcoins = 0
room_counter = 0
for el in dungeons_room:
    command, token = el.split()
    token = int(token)
    room_counter += 1
    if command == 'potion':
        if curent_health + token > 100:
            token = 100 - curent_health
            curent_health = 100
        else:
            curent_health += token
        print(f'You healed for {token} hp.')
        print(f"Current health: {curent_health} hp.")
    elif command == 'chest':
        bitcoins += token
        print(f"You found {token} bitcoins.")
    else:
        if curent_health - token <= 0:
            curent_health -= token
            print(f"You died! Killed by {command}.")
            print(f'Best room: {room_counter}')
            break
        else:
            curent_health -= token
            print(f"You slayed {command}.")

if curent_health > 0:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {curent_health}")
