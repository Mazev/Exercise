electrons = int(input())

electron_list = []
electrons_level = 0
while electrons > 0:
    electrons_level += 1
    electrons_needet = 2 * electrons_level **2
    if electrons < electrons_needet:
        electron_list.append(electrons)
        break
    electrons -= electrons_needet
    electron_list.append(electrons_needet)

print(electron_list)