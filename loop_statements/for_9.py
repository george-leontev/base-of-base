a = int(input('Number A = '))
b = int(input('Number B = '))
sum = int()

for n in range(a, b + 1):
    sum = sum + n**2

print(sum)