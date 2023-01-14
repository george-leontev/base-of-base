n = int(input('Decree = '))
a = int(input('Number = '))
sum = 1
sign = 1
p = 1

for _ in range(1, n + 1):
    sign = sign * (-1)
    p = p * a
    sum = sum + sign * p

print(f'Sum = {sum}')