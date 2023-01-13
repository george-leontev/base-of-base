a = int(input('Amount of terms = '))
term = 1
sign = 1
sum = 0

for x in range(1, a + 1):
    term = term + 0.1
    sum = sum + sign * term
    sign = sign * (-1)

print(f'Sum = {sum:.2}')
print(f'Term = {term:.2}')