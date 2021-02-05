courses_dict = {}

command = input()
while not command == 'end':
    course_name, student_name = command.split(' : ')
    if not course_name in courses_dict:
        courses_dict[course_name] = []
    courses_dict[course_name].append(student_name)

    command = input()

courses_dict = dict(sorted(courses_dict.items(), key=lambda x: len(x[1]), reverse = True))
for course_name, student_name in courses_dict.items():
    student_name.sort()
for course_name, student_name in courses_dict.items():
    print(f'{course_name}: {len(student_name)}')
    for i in student_name:
        print(f'-- {i}')
