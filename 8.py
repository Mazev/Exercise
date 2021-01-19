cards = input().split()

team_a = [1] * 11
team_b = [1] * 11
team_a_counter = 11
team_b_counter = 11
game_is_terminated = False

for el in cards:
    tokens = el.split('-')
    team = tokens[0]
    num_player = int(tokens[1])
    index = num_player - 1

    if team == 'A':
        if team_a[index] == 0:
            continue
        team_a[index] = 0
        team_a_counter -= 1
    else:
        if team_b[index] == 0:
            continue
        team_b[index] = 0
        team_b_counter -=1

    if team_a_counter <7 or team_b_counter <7:
        game_is_terminated = True
        break

print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
if game_is_terminated == True:
    print("Game was terminated")

