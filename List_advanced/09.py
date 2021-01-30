many_rooms = int(input())

room_counter = 0
free_chairs_counter = 0
negative = 0

for oom in range(many_rooms):
    command = input()
    room_counter += 1
    chairs, people = command.split()
    chairs = len(chairs)
    people = int(people)

    if chairs >= people:
        free_chairs = chairs - people
        free_chairs_counter += free_chairs
    else:
        need_chairs = people - chairs
        negative +=1
        print(f'{need_chairs} more chairs needed in room {room_counter}')



if negative ==0:
    print(f"Game On, {free_chairs_counter} free chairs left")

