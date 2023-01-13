n = int(input('Amount of terms = '))
sum = 0
term = 1

for x in range(1, n + 1):
    sum = sum + term
    term = term + 2

print(f'Sum = {sum:.2f}')
print(f'Term = {term:.2f}')