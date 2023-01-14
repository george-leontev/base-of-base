n = int(input('Amount of terms = '))
x = int(input('Number = '))
factorial = 1
sum = 1
degree = 1

for y in range(1, n + 1):
    factorial = factorial * y
    degree = degree * x
    sum = sum + degree / factorial

print(sum)