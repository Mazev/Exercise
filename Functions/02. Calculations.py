command = input()
num_1 = int(input())
num_2 = int(input())


def calculations(operations, a, b):
    results = None
    if operations == 'multiply':
        results = a * b
    elif operations == 'divide':
        results = a // b
    elif operations == 'add':
        results = a + b
    elif operations == 'subtract':
        results = a - b
    return results


print(calculations(command, num_1, num_2))
