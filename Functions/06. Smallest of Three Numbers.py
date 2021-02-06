num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def small_of_the_three_num(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


print(small_of_the_three_num(num_1, num_2, num_3))
