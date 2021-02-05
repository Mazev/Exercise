n = int(input())

students = {}
for _ in range(n):
    name = input()
    grades = float(input())
    if not name in students:
        students[name] = []
    students[name].append(grades)

filtered_students = {}

for name, grades in students.items():
    average_grades = sum(grades) / len(grades)
    if average_grades >=4.50:
        filtered_students[name] = average_grades

for name, average_grades in sorted(filtered_students.items(), key= lambda x: x[1], reverse= True):
    print(f'{name} -> {average_grades:.2f}')