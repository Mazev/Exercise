n = int(input())

positive_list = []
negative_list = []

for i in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive_list.append(numbers)
    else:
        negative_list.append(numbers)

print(positive_list)
print(negative_list)
print(f"Count of positives: {sum(positive_list)}. Sum of negatives: {sum(negative_list)}")