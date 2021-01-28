words = input().split()
palindrom = input()
new_list = []

for el in words:
    if el == el[::-1]:
        new_list.append(el)

counter = 0
for elements in new_list:
    if elements == palindrom:
        counter += 1

print(new_list)
print(f"Found palindrome {counter} times")