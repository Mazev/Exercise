health = 100
bitcoins = 0

rooms = list(map(str, input().split("|")))
rooms_counter = 0

for room in rooms:
    command, number = room.split()
    number = int(number)
    rooms_counter += 1
    if command == "potion":
        if health + number > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.\n"
              f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        if health - number <= 0:
            health -= number
            print(f"You died! Killed by {command}.\n"
                  f"Best room: {rooms_counter}")
            break

        else:
            health -= number
            print(f"You slayed {command}.")

if health > 0:
    print(f"You've made it!\n"
          f"Bitcoins: {bitcoins}\n"
          f"Health: {health}")