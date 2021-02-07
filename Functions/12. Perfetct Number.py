number = int(input())


def perfect_num(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    return sum == num


perfect_num(number)
result = perfect_num(number)
if  result:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")