number_1 = int(input())
number_2 = int(input())


def factorial(a, b):
    factorial_num_1 = 1
    factorial_num_2 = 1
    for i in range(1, a + 1):
        factorial_num_1 = i * factorial_num_1
    for y in range(1, b + 1):
        factorial_num_2 = y * factorial_num_2
    divide = factorial_num_1 / factorial_num_2
    return divide


result = factorial(number_1, number_2)
print(f'{result:.2f}')
