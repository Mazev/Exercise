n = int(input())
token = input()

new_list = []
mach_word = []
for i in range(n):
    lines = input()
    new_list.append(lines)
    if token in lines:
        mach_word.append(lines)
print(new_list)
print(mach_word)