num = int(input())


def loading_bar(number):
    loading_list = ['.'] * 10
    result = number // 10
    for el in range(0, result):
        loading_list.pop(el)
        loading_list.insert(el, '%')
    return loading_list


filled = loading_bar(num)
if num < 100:
    print(f"{num}% [{''.join(filled)}]")
    print('Still loading...')
else:
    print('100% Complete!')
    print(f"[{''.join(filled)}]")
