n = int(input('Amount of terms = '))
product = 1
sum = 0

for x in range(1, n + 1):
    product = product * x
    sum = sum + 1 / product

print(f'Sum = {sum}')