a = int(input('a = '))
b = int(input('b = '))
n = 0

for x in range(a,b + 1):
    n += 1
    print(f'{n}. x -> {x}')

print(f'Sum of numbers - {n}')