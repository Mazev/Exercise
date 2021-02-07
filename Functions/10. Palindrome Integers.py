palindrome = input()


def palindrome_integers(a):
    token = a.split(', ')
    for el in token:
        if el == el[::-1]:
            print('True')
        else:
            print('False')


palindrome_integers(palindrome)
