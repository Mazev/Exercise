courses_dict = {}

command = input()
while not command == 'end':
    course_name, student_name = command.split(' : ')
    if not course_name in courses_dict:
        courses_dict[course_name] = student_name
    elif course_name in courses_dict and not student_name:
        courses_dict[student_name] = student_name


    command = input()

print(courses_dict)