words = input()

digt = {}

for el in words:
    if el == " ":
        continue
    if el in digt:
        digt[el] += 1
    if el not in digt:
        digt[el] = 0
        digt[el] += 0
        if el in digt:
            digt[el] += 1

for key, value in digt.items():
    print(f'{key} -> {value}')