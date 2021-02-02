employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
people_count = int(input())

people_count_per_hour = employee_1 + employee_2 + employee_3

hour_count = 0

while people_count > 0:
    hour_count += 1
    people_count-= people_count_per_hour
    if hour_count % 4 == 0:
        hour_count += 1
        continue

print(f"Time needed: {hour_count}h.")