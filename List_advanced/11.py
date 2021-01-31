list_of_numbers = list(map(int, input().split(', ')))

max_num = list(map(int, list_of_numbers))

for i in range(1, max(max_num) // 10 + 1):
    result = [max_num[j] for j in range(len(max_num)) if max_num[j] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i *10 }'s: {result}")
