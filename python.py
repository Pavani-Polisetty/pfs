numbers = list(map(int, input().split()))
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)