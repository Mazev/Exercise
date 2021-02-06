string = input()
repeat = int(input())


def repeat_string(text, number):
    results = text * number
    return results


print(repeat_string(string, repeat))