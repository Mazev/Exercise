character_1 = input()
character_2 = input()


def character_range(a, b):
    a = ord(a)
    b = ord(b)
    new_list = []
    for i in range(a + 1, b):
        new_list.append(chr(i))
    print(*new_list)


character_range(character_1, character_2)
