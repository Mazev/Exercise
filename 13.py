data_fire = input().split('#')
water = int(input())

HIGH_FIRE = range(81, 126)
MEDIUM_FIRE = range(51, 81)
LOW_FIRE = range(1, 51)

efor = 0
cells = []
for fire in data_fire:
    type, value = fire.split(' = ')
    value = int(value)
    if type == 'High' and not value in HIGH_FIRE:
        continue
    elif type == 'Medium' and not value in MEDIUM_FIRE:
        continue
    elif type == 'Low' and not value in LOW_FIRE:
        continue
    if water >= value:
        water -= value
        efor += value * 0.25
        cells.append(value)

print('Cells:')
for i in cells:
    print(f' - {i}')
print(f'Effort: {efor:.2f}')
print(f'Total Fire: {sum(cells)}')
