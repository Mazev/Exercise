initial_list = input().split('!')

data = input()
while not data == 'Go Shopping!':
    asd = data.split()
    if asd[0] == 'Urgent':
        item = asd[1]
        if not item in initial_list:
            initial_list.insert(0, item)
    elif asd[0] == 'Unnecessary':
        item = asd[1]
        if item in initial_list:
            initial_list.remove(item)
    elif asd[0] == 'Correct':
        old_item = asd[1]
        new_item = asd[2]
        if old_item in initial_list:
            index_old_item = initial_list.index(old_item)
            initial_list.remove(old_item)
            initial_list.insert(index_old_item, new_item)

    elif asd[0] == 'Rearrange':
        item = asd[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)
        else:
            continue

    data = input()

print(', '.join(initial_list))