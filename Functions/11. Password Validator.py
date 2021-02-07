password = input()


def password_validator(chek):
    is_valid = True
    integer_count = 0
    if not (6 <= len(chek) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")
    for el in chek:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if el.isdigit():
            integer_count += 1
    if integer_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


result = password_validator(password)

if result:
    print("Password is valid")
