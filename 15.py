events = input().split('|')

energy = 100
coins = 100

for event in events:
    event_name, number = event.split('-')
    number = int(number)

    if event_name == 'rest':
        gained_energy = 0
        if energy + number <= 100:
            gained_energy = number
            energy += gained_energy
        else:
            gained_energy = 100 - energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == 'order':
        energy -= 30
        if energy > 0:
            coins += number
            print(f"You earned {number} coins.")
        elif energy < 30:
            energy += 50
            print("You had to rest!")
            continue
    else:
        coins -= number
        if coins > 0:
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break

if energy > 0 and coins > 0:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")