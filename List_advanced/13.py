# students_count = int(input())
# count_of_lectures = int(input())
# bonus = int(input())
#
# max_bonus = 0
# attendance = 0
# while students_count > 0:
#     attendances_student = int(input())
#     total_bonus = attendances_student / count_of_lectures * (5 + bonus)
#     if max_bonus < total_bonus:
#         max_bonus = total_bonus
#         attendance = attendances_student
#     students_count -= 1
#     attendances_student = int(input())
#
# print(f'Max Bonus: {max_bonus}')
# print(f'The student has attended {enumerate} lectures.')



students_count = int(input())
count_of_lectures = int(input())
bonus = int(input())

max_bonus = 0
attendance = 0
for el in range(students_count):
    attendances_student = int(input())
    total_bonus = attendances_student / count_of_lectures * (5 + bonus)
    if max_bonus < total_bonus:
        max_bonus = total_bonus
        attendance = attendances_student


print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {attendance} lectures.')