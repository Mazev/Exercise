list_of_integers = input().split()
count = int(input())
integers = list(map(int, list_of_integers))

for i in range(count):
    integers.remove(min(integers))

print(integers)