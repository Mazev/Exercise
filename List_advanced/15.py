colecting_items = input().split(', ')

command = input()
while not command == 'Craft!':
    token, item = command.split(' - ')
    if token == 'Collect':
        if item not in colecting_items:
            colecting_items.append(item)
            if item in colecting_items:
                continue
    elif token == 'Drop':
        if item in colecting_items:
            colecting_items.remove(item)
    elif token == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in colecting_items:
            old_item_index = colecting_items.index(old_item)
            new_item_index = old_item_index + 1
            colecting_items.insert(new_item_index, new_item)
    elif token == 'Renew':
        if item in colecting_items:
            colecting_items.remove(item)
            colecting_items.append(item)

    command = input()

print(', '.join(colecting_items))
